"""
Edmonton Weather — Data Analysis
=================================
Generates heatmaps and long-term trend charts from the cleaned daily weather dataset.

Full-period stations used (2000–2026):
  EDMONTON BLATCHFORD        (27214)
  EDMONTON INTERNATIONAL CS  (27793)
  EDMONTON STONY PLAIN CS    (27492)
  EDMONTON STONY PLAIN       (1870)

Outputs:  Data Analysis/plots/
Run from: Weather Edmonton/  (parent of this folder)
"""

import os
from dataclasses import dataclass

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
from scipy import stats

# ── Constants ─────────────────────────────────────────────────────────────────

DATA_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "Clean Data", "edmonton_weather_clean.csv",
)
PLOTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plots")

FULL_PERIOD_STATION_IDS = {27214, 27793, 27492, 1870}
BASELINE_YEARS = range(2000, 2025)   # 2000–2024 inclusive

MONTH_LABELS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Gray-and-gold palette
DARK_BG    = "#1E1E1E"
PANEL_BG   = "#2A2A2A"
GOLD       = "#C9A84C"
LIGHT_TEXT = "#E0E0E0"
DIM_TEXT   = "#888888"
COLD_BLUE  = "#4A90D9"
WARM_RED   = "#D94A4A"


# ── Data helpers ───────────────────────────────────────────────────────────────

def load_clean_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["Date"])
    df["Year"]  = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    return df


def filter_full_period(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["Station ID"].isin(FULL_PERIOD_STATION_IDS)].copy()


def daily_station_average(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Average multiple stations into one representative daily value."""
    return df.groupby("Date")[columns].mean().reset_index()


def monthly_pivot(series: pd.Series, year_col: pd.Series,
                  month_col: pd.Series, agg: str = "mean") -> pd.DataFrame:
    """Build a Year × Month pivot from a flat series plus year/month columns."""
    tmp = pd.DataFrame({"year": year_col, "month": month_col, "val": series})
    grouped = tmp.groupby(["year", "month"])["val"].agg(agg).reset_index()
    pivot = grouped.pivot(index="year", columns="month", values="val")
    pivot.columns = MONTH_LABELS
    return pivot


# ── Shared styling ─────────────────────────────────────────────────────────────

def style_dark(fig: plt.Figure, axes) -> None:
    fig.patch.set_facecolor(DARK_BG)
    ax_list = axes if hasattr(axes, "__iter__") else [axes]
    for ax in ax_list:
        ax.set_facecolor(PANEL_BG)
        ax.tick_params(colors=LIGHT_TEXT, which="both")
        ax.xaxis.label.set_color(LIGHT_TEXT)
        ax.yaxis.label.set_color(LIGHT_TEXT)
        ax.title.set_color(LIGHT_TEXT)
        for spine in ax.spines.values():
            spine.set_color(DIM_TEXT)


def style_colorbar(cbar, label: str) -> None:
    cbar.set_label(label, color=LIGHT_TEXT)
    cbar.ax.yaxis.set_tick_params(color=LIGHT_TEXT)
    plt.setp(cbar.ax.yaxis.get_ticklabels(), color=LIGHT_TEXT)


def save(fig: plt.Figure, filename: str) -> None:
    path = os.path.join(PLOTS_DIR, filename)
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"  saved -> {os.path.relpath(path)}")


# ── Figure 1: Year × Month — Mean Temperature heatmap ─────────────────────────

def plot_heatmap_mean_temp(daily: pd.DataFrame) -> None:
    daily["Year"]  = daily["Date"].dt.year
    daily["Month"] = daily["Date"].dt.month
    pivot = monthly_pivot(
        daily["Mean Temperature (C)"],
        daily["Year"], daily["Month"], agg="mean",
    )

    fig, ax = plt.subplots(figsize=(15, 9))
    im = ax.imshow(
        pivot.values, aspect="auto", cmap="RdBu_r",
        vmin=-22, vmax=22, interpolation="nearest",
    )

    ax.set_xticks(range(12))
    ax.set_xticklabels(MONTH_LABELS, fontsize=11)
    ax.set_yticks(range(len(pivot)))
    ax.set_yticklabels(pivot.index, fontsize=9)
    ax.set_xlabel("Month", fontsize=12, labelpad=8)
    ax.set_ylabel("Year",  fontsize=12, labelpad=8)
    ax.set_title(
        "Edmonton — Mean Temperature by Year & Month  (°C)\n"
        "2000–2026  ·  4 Full-Period Stations",
        fontsize=14, pad=14,
    )

    cbar = fig.colorbar(im, ax=ax, fraction=0.025, pad=0.02)
    style_colorbar(cbar, "Mean Temp (°C)")
    style_dark(fig, ax)
    fig.tight_layout()
    save(fig, "fig1_heatmap_mean_temp.png")


# ── Figure 2: Year × Month — Monthly Total Precipitation heatmap ──────────────

def plot_heatmap_precipitation(daily: pd.DataFrame) -> None:
    # NaN → 0: structurally expected (no-precip days log nothing)
    daily = daily.copy()
    daily["Total Precipitation (mm)"] = daily["Total Precipitation (mm)"].fillna(0)
    daily["Year"]  = daily["Date"].dt.year
    daily["Month"] = daily["Date"].dt.month

    # Sum daily values per year-month
    pivot = monthly_pivot(
        daily["Total Precipitation (mm)"],
        daily["Year"], daily["Month"], agg="sum",
    )

    fig, ax = plt.subplots(figsize=(15, 9))
    im = ax.imshow(
        pivot.values, aspect="auto", cmap="YlGnBu",
        vmin=0, vmax=90, interpolation="nearest",
    )

    ax.set_xticks(range(12))
    ax.set_xticklabels(MONTH_LABELS, fontsize=11)
    ax.set_yticks(range(len(pivot)))
    ax.set_yticklabels(pivot.index, fontsize=9)
    ax.set_xlabel("Month", fontsize=12, labelpad=8)
    ax.set_ylabel("Year",  fontsize=12, labelpad=8)
    ax.set_title(
        "Edmonton — Monthly Total Precipitation by Year  (mm)\n"
        "2000–2026  ·  4 Full-Period Stations  ·  NaN days treated as 0",
        fontsize=14, pad=14,
    )

    cbar = fig.colorbar(im, ax=ax, fraction=0.025, pad=0.02)
    style_colorbar(cbar, "Total Precipitation (mm)")
    style_dark(fig, ax)
    fig.tight_layout()
    save(fig, "fig2_heatmap_precipitation.png")


# ── Figure 3: Year × Month — Snow on Ground heatmap ───────────────────────────

def plot_heatmap_snow_on_ground(daily: pd.DataFrame) -> None:
    daily = daily.copy()
    daily["Year"]  = daily["Date"].dt.year
    daily["Month"] = daily["Date"].dt.month
    pivot = monthly_pivot(
        daily["Snow on Ground (cm)"],
        daily["Year"], daily["Month"], agg="mean",
    )

    fig, ax = plt.subplots(figsize=(15, 9))
    im = ax.imshow(
        pivot.values, aspect="auto", cmap="Blues",
        vmin=0, vmax=35, interpolation="nearest",
    )

    ax.set_xticks(range(12))
    ax.set_xticklabels(MONTH_LABELS, fontsize=11)
    ax.set_yticks(range(len(pivot)))
    ax.set_yticklabels(pivot.index, fontsize=9)
    ax.set_xlabel("Month", fontsize=12, labelpad=8)
    ax.set_ylabel("Year",  fontsize=12, labelpad=8)
    ax.set_title(
        "Edmonton — Average Snow on Ground by Year & Month  (cm)\n"
        "2000–2026  ·  4 Full-Period Stations",
        fontsize=14, pad=14,
    )

    cbar = fig.colorbar(im, ax=ax, fraction=0.025, pad=0.02)
    style_colorbar(cbar, "Avg Snow on Ground (cm)")
    style_dark(fig, ax)
    fig.tight_layout()
    save(fig, "fig3_heatmap_snow_on_ground.png")


# ── Figure 4: Annual mean temperature trend (OLS regression) ──────────────────

def plot_annual_temp_trend(daily: pd.DataFrame) -> None:
    daily = daily.copy()
    daily["Year"] = daily["Date"].dt.year

    annual = (
        daily.groupby("Year")["Mean Temperature (C)"]
        .mean()
        .reset_index()
        .rename(columns={"Mean Temperature (C)": "MeanTemp"})
    )

    # OLS on baseline years only; project across full range
    baseline = annual[annual["Year"].isin(BASELINE_YEARS)]
    slope, intercept, r, p, _ = stats.linregress(baseline["Year"], baseline["MeanTemp"])
    x_fit = np.array([annual["Year"].min(), annual["Year"].max()])
    y_fit = intercept + slope * x_fit

    fig, ax = plt.subplots(figsize=(13, 6))

    # Bars coloured by above/below grand mean
    grand_mean = baseline["MeanTemp"].mean()
    colors = [WARM_RED if t >= grand_mean else COLD_BLUE for t in annual["MeanTemp"]]
    ax.bar(annual["Year"], annual["MeanTemp"], color=colors, alpha=0.75, zorder=2)

    # Regression line
    ax.plot(x_fit, y_fit, color=GOLD, linewidth=2.2, zorder=3,
            label=f"Trend (2000–2024):  {slope:+.3f} °C/yr   r²={r**2:.3f}   p={p:.3f}")

    # Grand-mean reference
    ax.axhline(grand_mean, color=DIM_TEXT, linewidth=1, linestyle="--", zorder=1)

    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Annual Mean Temperature (°C)", fontsize=12)
    ax.set_title(
        "Edmonton — Annual Mean Temperature & Long-Term Trend\n"
        "2000–2026  ·  4 Full-Period Stations",
        fontsize=14, pad=14,
    )
    legend = ax.legend(fontsize=10)
    legend.get_frame().set_facecolor(PANEL_BG)
    for text in legend.get_texts():
        text.set_color(LIGHT_TEXT)

    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.1f°"))
    style_dark(fig, ax)
    fig.tight_layout()
    save(fig, "fig4_annual_temp_trend.png")


# ── Figure 5: Extreme cold days per year (mean < −20 °C) ──────────────────────

def plot_extreme_cold_days(daily: pd.DataFrame) -> None:
    daily = daily.copy()
    daily["Year"] = daily["Date"].dt.year

    cold = (
        daily[daily["Mean Temperature (C)"] < -20]
        .groupby("Year")["Date"]
        .nunique()
        .reindex(range(daily["Year"].min(), daily["Year"].max() + 1), fill_value=0)
    )

    fig, ax = plt.subplots(figsize=(13, 6))
    ax.bar(cold.index, cold.values, color=COLD_BLUE, alpha=0.85, zorder=2)
    ax.axhline(cold.mean(), color=GOLD, linewidth=1.8, linestyle="--",
               label=f"25-yr avg:  {cold[list(BASELINE_YEARS)].mean():.1f} days")

    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Days with Mean Temp < −20 °C", fontsize=12)
    ax.set_title(
        "Edmonton — Extreme Cold Days per Year  (mean temp < −20 °C)\n"
        "2000–2026  ·  4 Full-Period Stations",
        fontsize=14, pad=14,
    )
    legend = ax.legend(fontsize=10)
    legend.get_frame().set_facecolor(PANEL_BG)
    for text in legend.get_texts():
        text.set_color(LIGHT_TEXT)

    style_dark(fig, ax)
    fig.tight_layout()
    save(fig, "fig5_extreme_cold_days.png")


# ── Figure 6: Extreme hot days per year (mean > 25 °C) ────────────────────────

def plot_extreme_hot_days(daily: pd.DataFrame) -> None:
    daily = daily.copy()
    daily["Year"] = daily["Date"].dt.year

    hot = (
        daily[daily["Mean Temperature (C)"] > 25]
        .groupby("Year")["Date"]
        .nunique()
        .reindex(range(daily["Year"].min(), daily["Year"].max() + 1), fill_value=0)
    )

    fig, ax = plt.subplots(figsize=(13, 6))
    ax.bar(hot.index, hot.values, color=WARM_RED, alpha=0.85, zorder=2)
    ax.axhline(hot.mean(), color=GOLD, linewidth=1.8, linestyle="--",
               label=f"25-yr avg:  {hot[list(BASELINE_YEARS)].mean():.1f} days")

    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Days with Mean Temp > 25 °C", fontsize=12)
    ax.set_title(
        "Edmonton — Extreme Hot Days per Year  (mean temp > 25 °C)\n"
        "2000–2026  ·  4 Full-Period Stations  ·  2021 heat dome visible",
        fontsize=14, pad=14,
    )
    legend = ax.legend(fontsize=10)
    legend.get_frame().set_facecolor(PANEL_BG)
    for text in legend.get_texts():
        text.set_color(LIGHT_TEXT)

    style_dark(fig, ax)
    fig.tight_layout()
    save(fig, "fig6_extreme_hot_days.png")


# ── Figure 7: Freeze-thaw cycles per year ─────────────────────────────────────

def plot_freeze_thaw_cycles(daily: pd.DataFrame) -> None:
    """Count days where min < 0 °C AND max > 0 °C in the same day."""
    daily = daily.copy()
    daily["Year"] = daily["Date"].dt.year

    mask = (
        daily["Minimum Temperature (C)"].lt(0) &
        daily["Maximum Temperature (C)"].gt(0)
    )
    freeze_thaw = (
        daily[mask]
        .groupby("Year")["Date"]
        .nunique()
        .reindex(range(daily["Year"].min(), daily["Year"].max() + 1), fill_value=0)
    )

    baseline_mean = freeze_thaw[list(BASELINE_YEARS)].mean()

    fig, ax = plt.subplots(figsize=(13, 6))
    ax.bar(freeze_thaw.index, freeze_thaw.values, color=GOLD, alpha=0.8, zorder=2)
    ax.axhline(baseline_mean, color=LIGHT_TEXT, linewidth=1.8, linestyle="--",
               label=f"25-yr avg:  {baseline_mean:.1f} days")

    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Freeze-Thaw Days", fontsize=12)
    ax.set_title(
        "Edmonton — Freeze-Thaw Cycles per Year\n"
        "Days where min < 0 °C and max > 0 °C  ·  2000–2026  ·  4 Full-Period Stations",
        fontsize=14, pad=14,
    )
    legend = ax.legend(fontsize=10)
    legend.get_frame().set_facecolor(PANEL_BG)
    for text in legend.get_texts():
        text.set_color(LIGHT_TEXT)

    style_dark(fig, ax)
    fig.tight_layout()
    save(fig, "fig7_freeze_thaw_cycles.png")


# ── Figure 8: Annual temperature anomaly vs 2000–2024 baseline ────────────────

def plot_annual_temp_anomaly(daily: pd.DataFrame) -> None:
    daily = daily.copy()
    daily["Year"] = daily["Date"].dt.year

    annual = daily.groupby("Year")["Mean Temperature (C)"].mean()
    baseline_mean = annual[list(BASELINE_YEARS)].mean()
    anomaly = annual - baseline_mean

    colors = [WARM_RED if a >= 0 else COLD_BLUE for a in anomaly]

    fig, ax = plt.subplots(figsize=(13, 6))
    ax.bar(anomaly.index, anomaly.values, color=colors, alpha=0.85, zorder=2)
    ax.axhline(0, color=LIGHT_TEXT, linewidth=1.2, zorder=3)

    # Label the two most extreme years
    for year in [anomaly.idxmax(), anomaly.idxmin()]:
        val = anomaly[year]
        ax.annotate(
            f"{year}\n{val:+.2f}°",
            xy=(year, val),
            xytext=(year, val + (0.25 if val >= 0 else -0.35)),
            ha="center", fontsize=9, color=LIGHT_TEXT,
        )

    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Temperature Anomaly (°C)", fontsize=12)
    ax.set_title(
        "Edmonton — Annual Temperature Anomaly vs 2000–2024 Baseline\n"
        "4 Full-Period Stations  ·  Baseline mean: "
        f"{baseline_mean:.2f} °C",
        fontsize=14, pad=14,
    )
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%+.1f°"))
    style_dark(fig, ax)
    fig.tight_layout()
    save(fig, "fig8_annual_temp_anomaly.png")


# ── Main ───────────────────────────────────────────────────────────────────────

def main() -> None:
    os.makedirs(PLOTS_DIR, exist_ok=True)

    print("Loading data …")
    raw   = load_clean_data(DATA_PATH)
    full  = filter_full_period(raw)

    # Build one representative daily series (average across the 4 stations)
    daily = daily_station_average(
        full,
        ["Mean Temperature (C)", "Maximum Temperature (C)",
         "Minimum Temperature (C)", "Total Precipitation (mm)",
         "Snow on Ground (cm)"],
    )

    print("Generating figures …")
    plot_heatmap_mean_temp(daily)
    plot_heatmap_precipitation(daily)
    plot_heatmap_snow_on_ground(daily)
    plot_annual_temp_trend(daily)
    plot_extreme_cold_days(daily)
    plot_extreme_hot_days(daily)
    plot_freeze_thaw_cycles(daily)
    plot_annual_temp_anomaly(daily)

    print("\nDone. All figures written to:", PLOTS_DIR)


if __name__ == "__main__":
    main()
