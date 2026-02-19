# Edmonton Weather — Exploratory Data Analysis Summary
**Source:** Environment Canada Daily Weather Records
**Period:** January 1, 2000 – February 17, 2026
**Stations analysed (full-period):** 4 of 9 (see Section 1 for exclusions)
**Records after cleaning:** 57,901 rows across 9 stations

---

## 1. Dataset Structure and Station Coverage

### What the data contains
Each row represents one station's weather observation for a single calendar day. The cleaned dataset retains ten columns:

| Column | Description |
|---|---|
| Station ID | Numeric identifier assigned by Environment Canada |
| Station Name | Human-readable name of the weather station |
| Date | Calendar date (YYYY/MM/DD) |
| Maximum Temperature (C) | Highest temperature recorded that day |
| Minimum Temperature (C) | Lowest temperature recorded that day |
| Mean Temperature (C) | Average of maximum and minimum for the day |
| Total Rain (mm) | Liquid precipitation, millimetres |
| Total Snow (cm) | Snowfall accumulation, centimetres |
| Total Precipitation (mm) | Combined rain + snow-water equivalent |
| Snow on Ground (cm) | Depth of snowpack at end of day |

### Station inventory and active periods

| Station | Station ID | First Year | Last Year | Years Active | Avg Days/Year |
|---|---|---|---|---|---|
| EDMONTON BLATCHFORD | 27214 | 2000 | 2026 | 27 | 350 |
| EDMONTON INTERNATIONAL CS | 27793 | 2000 | 2026 | 27 | 347 |
| EDMONTON STONY PLAIN CS | 27492 | 2000 | 2026 | 27 | 349 |
| EDMONTON STONY PLAIN | 1870 | 2000 | 2026 | 27 | 338 |
| EDMONTON NAMAO AWOS A | 30907 | 2000 | 2022 | 23 | 314 |
| EDMONTON SOUTH CAMPUS | 53718 | 2017 | 2024 | 7 | 289 |
| EDMONTON VILLENEUVE A | 51758 | 2013 | 2026 | 14 | 303 |
| EDMONTON INTL A | 50149 | 2012 | 2026 | 15 | 334 |
| EDMONTON NAMAO A | 1868 | 2000 | 2002 | 3 | 245 |

**Stations excluded from the 2025 comparison** (Section 4 onward):
- **EDMONTON NAMAO AWOS A** — last active year 2022; no 2025 data
- **EDMONTON NAMAO A** — decommissioned after 2002; only 3 years of records
- **EDMONTON SOUTH CAMPUS** — operational 2017–2024 only; no 2025 data
- **EDMONTON INTL A** — opened 2012; does not span the full baseline period
- **EDMONTON VILLENEUVE A** — opened 2013; does not span the full baseline period

The four **full-period stations** (2000–2026, with 2025 data) used for all comparative analysis are:
> EDMONTON BLATCHFORD · EDMONTON INTERNATIONAL CS · EDMONTON STONY PLAIN · EDMONTON STONY PLAIN CS

### Data quality notes
- **Temperature columns** are ~98% complete — missing values are sparse and random, not clustered on any particular station or season.
- **Precipitation columns** carry ~55–57% null rates. The vast majority of these nulls represent days where no precipitation fell and the sensor returned no reading, not genuine data gaps. Days with zero recorded precipitation are structurally different from missing observations.
- The three source raw files were exact byte-for-byte duplicates; only one was used.
- Four non-Edmonton stations present in the raw data (LEGAL, NEW SAREPTA, OLIVER, THORSBY) were removed during cleaning.

---

## 2. Long-Term Temperature Profile (2000–2024 baseline)

### Annual average
Across all four full-period stations, the long-term daily mean temperature is **+3.85 °C**. This reflects Edmonton's strongly continental sub-humid climate: long cold winters and short warm summers, with a wide annual swing.

### Monthly temperature normals
The table below shows the 25-year average (2000–2024) for each month across all full-period stations. These values serve as the baseline for all 2025 comparisons in Section 4.

| Month | Avg Min (°C) | Avg Mean (°C) | Avg Max (°C) |
|---|---|---|---|
| January | −15.3 | −9.4 | −3.4 |
| February | −14.5 | −8.7 | −2.8 |
| March | −8.6 | −3.9 | +0.9 |
| April | −1.5 | +4.0 | +9.7 |
| May | +4.2 | +11.0 | +17.9 |
| June | +8.5 | +15.1 | +21.7 |
| **July** | **+10.9** | **+17.7** | **+24.4** |
| August | +9.5 | +16.3 | +23.1 |
| September | +4.1 | +11.6 | +19.1 |
| October | −1.9 | +4.7 | +11.3 |
| November | −9.0 | −3.5 | +2.0 |
| **December** | **−14.7** | **−9.5** | **−4.3** |

- The **annual temperature swing** from coldest to warmest monthly mean is approximately **27 °C** — a hallmark of continental climates far from ocean moderation.
- Temperatures remain **below freezing on average from November through March** (five months of below-zero mean temperatures).
- The **shoulder seasons** (April, October) are transitional — freeze/thaw cycles are common and precipitation can fall as either rain or snow.

### Temperature distribution (Fig 5)
The violin plots reveal that winter months (December–February) have the widest spread of daily temperatures, meaning individual days can range dramatically — from near-zero Chinook warmth to deep Arctic cold well below −30 °C. Summer months (July–August) are tightly concentrated, with relatively few extreme outliers.

### All-time temperature records (all 9 stations, 2000–2026)
| Record | Value | Date | Station |
|---|---|---|---|
| Coldest daily mean | −40.2 °C | January 12, 2024 | EDMONTON INTL A |
| Coldest daily minimum | −46.6 °C | January 12, 2024 | EDMONTON INTERNATIONAL CS |
| Warmest daily mean | +30.6 °C | June 30, 2021 | EDMONTON NAMAO AWOS A |
| Warmest daily maximum | +38.5 °C | July 1, 2021 | EDMONTON STONY PLAIN |

The January 2024 event was an extended Arctic outbreak affecting the entire region simultaneously — multiple stations recorded their all-time lows within the same 48-hour window. The June/July 2021 records correspond directly to the **Western Canadian Heat Dome**, an unprecedented atmospheric blocking event that drove temperatures across Western Canada to historic highs.

---

## 3. Long-Term Snowfall Profile (2000–2024 baseline)

### Snowfall seasonality
Snowfall is concentrated in the **October–April** window. The table below shows the average daily snowfall by month:

| Month | Avg Daily Snowfall (cm) | Avg Snow on Ground (cm) |
|---|---|---|
| January | 0.69 | 17.5 |
| February | 0.54 | 16.8 |
| March | 0.76 | 12.4 |
| April | 0.58 | 4.8 |
| May | 0.16 | 0.5 |
| June | 0.00 | 0.0 |
| July | 0.00 | 0.0 |
| August | 0.00 | 0.0 |
| September | 0.05 | 0.3 |
| October | 0.31 | 3.0 |
| November | 0.62 | 10.4 |
| December | 0.52 | 14.2 |

- **March sees the highest average daily snowfall** among winter months, reflecting that late-season storms can deliver significant accumulations even as spring approaches.
- **Snowpack (snow on ground) peaks in January–February** at roughly 16–18 cm on average, lagging slightly behind peak snowfall months because the pack accumulates progressively through winter.
- Summer months are entirely snow-free in the historical record.

### All-time snowfall records
| Record | Value | Date | Station |
|---|---|---|---|
| Largest single-day snowfall | 33.0 cm | February 25, 2024 | EDMONTON STONY PLAIN |
| Deepest snowpack recorded | 70.0 cm | January 18, 2011 | EDMONTON STONY PLAIN |

Edmonton STONY PLAIN consistently records the highest snowfall figures among Edmonton-area stations, likely due to its slightly more exposed position and local topographic effects.

### Extreme temperature days (Fig 6)
- **Cold extremes** (daily mean < −20 °C) occur most frequently in 2009, 2019, and 2024. These years align with documented Arctic air mass intrusions into the Prairies.
- **Hot extremes** (daily mean > 25 °C) are rare in the record but spiked dramatically in **2021** due to the heat dome — an anomaly clearly visible above every other year in the chart.

---

## 4. 2025 vs Baseline Comparison
*Stations used: BLATCHFORD · INTERNATIONAL CS · STONY PLAIN · STONY PLAIN CS*
*Baseline: 2000–2024 average (25 years) — 2025 excluded from the mean to avoid self-comparison*

### Annual summary (Fig 12)
| Metric | Baseline Mean (2000–2024) | 2025 | Delta | Delta % |
|---|---|---|---|---|
| Mean Temperature (°C) | +3.85 | **+4.61** | **+0.76** | +19.7% |
| Maximum Temperature (°C) | +9.35 | **+10.30** | **+0.94** | +10.1% |
| Minimum Temperature (°C) | −1.67 | **−1.09** | **+0.58** | +34.7% |
| Total Snow (cm) — daily avg | 0.35 | 0.59 | +0.24 | +68.8% |
| Total Precipitation (mm) — daily avg | 1.17 | 0.98 | −0.19 | −16.2% |
| Snow on Ground (cm) — daily avg | 7.54 | **10.48** | **+2.94** | +39.0% |

**Overall, 2025 was a warmer-than-average year across all temperature metrics.** The annual mean temperature of +4.61 °C sits nearly 0.8 °C above the 25-year baseline. Both daily highs and daily lows were elevated. Despite being warmer on average, 2025 carried a notably deeper-than-average snowpack (+39%), driven by concentrated heavy snowfall events in specific months rather than a broadly snowier year.

---

### Monthly temperature breakdown (Figs 8 & 9)

| Month | Baseline Mean (°C) | 2025 (°C) | Delta (°C) | Assessment |
|---|---|---|---|---|
| January | −9.38 | −6.10 | **+3.28** | Well above average — mild January |
| February | −8.68 | −13.31 | **−4.63** | Well below average — very cold February |
| March | −3.87 | −1.59 | **+2.28** | Above average — early warmth |
| April | +4.03 | +6.48 | **+2.45** | Noticeably warmer spring |
| May | +11.04 | +13.45 | **+2.41** | Warm early summer |
| June | +15.07 | +15.07 | 0.00 | Exactly average |
| July | +17.66 | +16.86 | −0.81 | Slightly below average |
| August | +16.29 | +18.25 | **+1.96** | Warm late summer |
| September | +11.55 | +15.30 | **+3.75** | Exceptionally warm — standout month |
| October | +4.68 | +6.49 | **+1.81** | Above average autumn |
| November | −3.50 | −1.99 | **+1.51** | Warmer than average |
| December | −9.54 | −13.85 | **−4.31** | Well below average — very cold December |

**Key observations:**

- **September 2025 (+3.75 °C above baseline)** was the most anomalously warm month of the year. An unusually persistent warm airmass through late summer kept temperatures elevated well into fall — more than 3.75 °C above the 25-year average for the month.
- **February 2025 (−4.63 °C below baseline)** and **December 2025 (−4.31 °C below baseline)** were the two coldest anomalies of the year. These represent Arctic outbreaks that sharply broke from the otherwise warm pattern, bookending the year with intense cold at both ends.
- The **warm season (March through November)** was dominated by above-average temperatures in 10 of those 9 months; only July was marginally cooler than average.
- **June 2025** was statistically indistinguishable from the long-term average, the only month to land exactly on the baseline.
- The **cold anomaly in February** is particularly notable given January was +3.28 °C warm — a dramatic swing of over 7 °C in mean temperature between adjacent months, likely reflecting an abrupt shift in atmospheric circulation pattern.

---

### Monthly snowfall breakdown (Figs 10 & 11)

| Month | Baseline Avg (cm/day) | 2025 (cm/day) | Delta (cm/day) | Assessment |
|---|---|---|---|---|
| January | 0.69 | 1.58 | **+0.89** | Much snowier than average |
| February | 0.54 | 0.23 | −0.31 | Below average |
| March | 0.76 | 2.39 | **+1.63** | Heaviest snowfall anomaly of the year |
| April | 0.58 | 0.00 | −0.58 | No snow recorded |
| May | 0.16 | 0.00 | −0.16 | No snow recorded |
| June–September | 0.00 | 0.00 | 0.00 | Snow-free, as expected |
| October | 0.31 | 0.04 | −0.27 | Very little snow |
| November | 0.62 | 0.41 | −0.21 | Slightly below average |
| December | 0.52 | 2.26 | **+1.74** | Second heaviest anomaly |

**Key observations:**

- **March 2025** recorded the largest snowfall anomaly of the year at +1.63 cm/day above the baseline — notable because March is already the snowiest month on average, and 2025 amplified that further with heavy late-season storms.
- **December 2025** was also far snowier than average (+1.74 cm/day), contributing to a deep end-of-year snowpack despite the cold anomaly making conditions feel particularly harsh.
- **January 2025** was both warmer than average in temperature AND snowier than average — consistent with warmer, moister airmasses delivering more active precipitation before the February Arctic outbreak.
- **April and May 2025** recorded zero snowfall, whereas the baseline shows small but non-zero averages for those months. This aligns with the warmer spring temperatures in 2025.
- **Snow on Ground** averaged 10.48 cm in 2025 versus the baseline of 7.54 cm (+39%). The outsized snowpack relative to snowfall suggests that the cold anomaly months (February, December) slowed melt and preserved accumulation longer than typical years.

---

### Where 2025 sits historically (Fig 12)
At +4.61 °C annual mean, 2025 ranks as one of the warmer years in the 25-year record for the four full-period stations — but it is not the record warmest. The most anomalous years remain those with persistent warm patterns rather than 2025's alternating warm/cold structure. The 2025 pattern is better described as **volatile**: a warm year on average, but punctuated by two severe cold outbreaks (February and December) and exceptional warmth in the shoulder seasons.

---

## 5. Early 2026 vs Baseline (January & February 1–17)
*Stations used: BLATCHFORD · INTERNATIONAL CS · STONY PLAIN · STONY PLAIN CS*
*Baseline: 2000–2024 average for the same calendar days — 2026 excluded from the mean*
*Note: February data covers days 1–17 only (dataset ends February 17, 2026). The baseline for February was also restricted to days 1–17 to ensure a like-for-like comparison.*

### Overall summary by period (Figs 13–16)

| Period | Metric | Baseline (2000–2024) | 2026 | Delta | Delta % |
|---|---|---|---|---|---|
| January (full month) | Mean Temp (°C) | −9.38 | **−7.53** | **+1.84** | +19.7% |
| January (full month) | Max Temp (°C) | −4.58 | **−2.64** | **+1.94** | +42.3% |
| January (full month) | Min Temp (°C) | −14.15 | **−12.43** | **+1.73** | +12.2% |
| January (full month) | Daily Snowfall (cm) | 0.69 | 0.56 | −0.13 | −18.3% |
| January (full month) | Daily Precip (mm) | 0.52 | 0.34 | −0.18 | −34.6% |
| January (full month) | Snow on Ground (cm) | 15.74 | **31.07** | **+15.34** | **+97.5%** |
| February (days 1–17) | Mean Temp (°C) | −9.06 | **−0.46** | **+8.61** | +95.0% |
| February (days 1–17) | Max Temp (°C) | −4.08 | **+4.12** | **+8.20** | +200.8% |
| February (days 1–17) | Min Temp (°C) | −14.01 | **−5.04** | **+8.97** | +64.0% |
| February (days 1–17) | Daily Snowfall (cm) | 0.49 | 1.33 | **+0.84** | +171.0% |
| February (days 1–17) | Daily Precip (mm) | 0.44 | 0.84 | **+0.40** | +89.5% |
| February (days 1–17) | Snow on Ground (cm) | 17.03 | **22.92** | **+5.88** | +34.5% |

---

### January 2026 — Warmer and deeply anomalous snowpack (Fig 13, 14, 15, 16)

January 2026 was **warmer than average across all three temperature metrics**, but the defining feature of the month was its snowpack — snow on ground averaged **31.07 cm**, nearly **double the 25-year baseline of 15.74 cm** (+97.5%). This is the single largest positive snowpack anomaly observed across either the 2025 or 2026 partial comparisons.

**Temperature detail:**
- The monthly mean of −7.53 °C was 1.84 °C above the baseline, continuing the pattern of above-average January temperatures also seen in January 2025 (+3.28 °C).
- Daily highs averaged −2.64 °C versus the baseline −4.58 °C; daily lows averaged −12.43 °C versus the baseline −14.15 °C. Both the top and the bottom of the daily range were shifted warmer.
- Despite the warmer average, January 2026 contained significant cold spikes. The **record low for the month was −30.4 °C on January 23 at EDMONTON INTERNATIONAL CS**, and the mean temperature ranged from −23.9 °C to +7.8 °C across the month — a spread of over 31 °C, illustrating the volatility typical of Edmonton winters when Chinook events alternate with Arctic outbreaks.
- The **record high of +13.0 °C was reached on January 14 at EDMONTON STONY PLAIN**, which is an exceptional mid-winter maximum for Edmonton and consistent with a Chinook event.

**Snowpack detail:**
- Despite slightly below-average daily snowfall (0.56 cm/day vs baseline 0.69 cm/day), the snowpack was nearly twice the normal depth. This apparent contradiction is explained by the **carryover from December 2025**, which was a very heavy snowfall month (+1.74 cm/day above baseline), combined with cold temperatures in early January that preserved rather than melted the accumulated pack.
- The deepest observed snowpack in January 2026 reached **47.0 cm at EDMONTON BLATCHFORD on January 4** — recorded just days into the new year, reflecting how the late-2025 snowfall directly fed into the 2026 snowpack.
- The maximum single-day snowfall event was **7.2 cm on January 1 at EDMONTON STONY PLAIN**.

---

### February 2026 (days 1–17) — The most extreme warm anomaly in the dataset (Fig 13, 14, 15, 16)

The first 17 days of February 2026 stand out as the most dramatic temperature anomaly in this entire analysis — more extreme than any individual month in 2025, and more extreme than January 2026.

**Temperature detail:**
- The mean temperature for February 1–17 was **−0.46 °C**, compared to the baseline of **−9.06 °C** for the same period. This is a departure of **+8.61 °C** — nearly 9 degrees above the 25-year average.
- The average daily maximum for this period was **+4.12 °C** — above freezing — against a baseline of **−4.08 °C**. This means the typical daily high in February 2026 crossed 0 °C while the baseline sits almost 4 °C below freezing. That is a shift of **+8.20 °C** on the daily high alone, and a **200.8% departure** relative to the baseline value.
- The average daily minimum of −5.04 °C was 8.97 °C above the baseline of −14.01 °C — again, a near-9-degree departure.
- The **record high for the period was +12.0 °C on February 5 at EDMONTON STONY PLAIN**, which is a temperature more characteristic of late April than early February.
- The **record low was −23.5 °C on February 17 at EDMONTON STONY PLAIN CS** — notably the last day of available data, suggesting an Arctic intrusion may have been underway at the end of the observation window.
- The temperature range across the period (−18.5 °C to +8.8 °C in daily means) shows that even within this anomalously warm fortnight, cold events were not entirely absent.

**To put the February 2026 anomaly in context:** the 25-year baseline for February 1–17 is −9.06 °C. In 2025, the full February averaged −13.31 °C (the coldest month of 2025, well below baseline). In 2026, the first 17 days of the same month averaged −0.46 °C. That is a swing of **nearly 13 °C between the same calendar period in consecutive years.**

**Snowfall and snowpack detail:**
- Daily snowfall averaged 1.33 cm/day — **171% above the baseline of 0.49 cm/day** — making February 2026 significantly snowier than average despite (or partly because of) the warm temperatures, which favour heavier, wetter snowfall events.
- The **largest single-day snowfall event was 12.0 cm on February 16 at EDMONTON STONY PLAIN** — a major snowfall event that occurred just one day before the dataset ends.
- Snow on ground averaged 22.92 cm, compared to a baseline of 17.03 cm (+34.5%). The snowpack remains elevated but is lower than January's anomaly, consistent with some melt from the above-freezing daytime highs.
- By February 17, the snowpack had climbed back to **39.0 cm at EDMONTON BLATCHFORD**, likely reflecting the large February 16 snowfall event.

---

### Per-station consistency (Fig 16)
The warm anomaly in February 2026 was consistent across all four full-period stations, with similar deltas at each location. This confirms the anomaly is a regional atmospheric signal, not a measurement artifact at a single station. January 2026 snowpack anomaly was also station-consistent, with all four stations showing snowpack roughly double their baseline values.

---

## 6. Summary of Key Findings

| Theme | Finding |
|---|---|
| Long-term climate | Edmonton has a strongly continental climate — ~27 °C annual swing, five sub-zero months |
| Warmest / coldest month | July avg +17.7 °C; December avg −9.5 °C |
| All-time cold | −46.6 °C minimum (Jan 12, 2024 — INTERNATIONAL CS) |
| All-time heat | +38.5 °C maximum (Jul 1, 2021 — STONY PLAIN, heat dome event) |
| 2025 overall | Warmer than average (+0.76 °C) but with extreme cold in Feb and Dec |
| 2025 standout warmth | September (+3.75 °C above baseline) |
| 2025 standout cold | February (−4.63 °C) and December (−4.31 °C) below baseline |
| 2025 snowfall | Concentrated in Jan, Mar, Dec — snowpack 39% above average |
| Jan 2026 | Above average temperature (+1.84 °C); snowpack nearly double baseline (+97.5%) |
| Feb 2026 (1–17) | Most extreme warm anomaly in dataset: +8.61 °C above baseline — avg max above freezing |
| Feb 2026 snowfall | +171% above baseline daily snowfall; 12 cm storm on Feb 16 |
| Year-over-year Feb swing | February mean: −13.3 °C in 2025 → −0.5 °C in 2026 — a 13 °C shift in one year |
| Data quality | ~2% temperature nulls; ~57% precipitation nulls (structurally expected) |
| Best long-run stations | BLATCHFORD and STONY PLAIN CS — most complete 2000–2026 records |

---

## 7. Figures and Files in This Folder

| File | Description |
|---|---|
| `fig1_coverage_heatmap.png` | Station × year data coverage (% days with temp data) |
| `fig2_monthly_temp_normals.png` | Monthly avg min / mean / max with ribbon chart |
| `fig3_annual_temp_trend.png` | Annual mean temperature + linear trend by primary station |
| `fig4_snowfall.png` | Monthly avg snowfall + annual totals |
| `fig5_temp_violin.png` | Daily temperature distribution by month (violin plot) |
| `fig6_extreme_days.png` | Count of extreme cold/hot days per year |
| `fig7_snow_on_ground.png` | Average snow on ground depth by month |
| `fig8_2025_vs_baseline_mean_temp.png` | 2025 vs baseline monthly mean temperature with delta labels |
| `fig9_2025_vs_baseline_max_min.png` | 2025 vs baseline monthly max and min temperatures |
| `fig10_2025_vs_baseline_snowfall.png` | 2025 vs baseline monthly snowfall |
| `fig11_2025_vs_baseline_snow_on_ground.png` | 2025 vs baseline snow on ground |
| `fig12_annual_temp_context.png` | All-year mean temperature bar chart with 2025 highlighted |
| `fig13_2026_daily_mean_temp.png` | Day-by-day mean temperature: Jan & Feb 2026 vs baseline |
| `fig14_2026_monthly_all_metrics.png` | Jan & Feb 2026 vs baseline for all six key metrics |
| `fig15_2026_daily_snow.png` | Daily snowfall and snow on ground: Jan & Feb 2026 vs baseline |
| `fig16_2026_per_station.png` | Per-station comparison: mean temp and snowpack for Jan & Feb 2026 |
| `descriptive_stats.csv` | Overall descriptive statistics (all numeric columns) |
| `descriptive_stats_by_station.csv` | Descriptive statistics broken out per station |
| `2025_vs_baseline_monthly.csv` | Full monthly comparison table: baseline vs 2025 vs delta |
| `2025_vs_baseline_annual.csv` | Annual summary: baseline vs 2025 vs delta for all metrics |
| `2026_vs_baseline_summary.csv` | Jan & Feb 2026 vs baseline summary for all key metrics |
| `2026_vs_baseline_by_station.csv` | Same breakdown per individual station |

---

*Generated 2026-02-18 — Stage 1 (data cleaning), Stage 2 (EDA), Stage 3 (2025 & 2026 comparisons) complete.*
*Full-period stations used for comparison: EDMONTON BLATCHFORD · EDMONTON INTERNATIONAL CS · EDMONTON STONY PLAIN · EDMONTON STONY PLAIN CS*
