# AI Workflow Log
Codex session: October 15, 2026, starting 7:00 AM.
Entries reconstructed from the exported session transcript on [today's date].
Prompts were drafted with help from Claude before the session; Claude also
wrote a reference script I used to check Codex's results.

## Prompt 1 – October 15, 2026, 7:00 AM session
**Prompt:** Load AmesHousing.csv and report rows, columns, data types, and missing values for SalePrice, Gr Liv Area, and Neighborhood. Don't create any files yet.
**Purpose:** Check the data before creating any files.
**Codex produced:** [row/column counts it reported]
**Accepted / Modified / Rejected:** [ ]
**Verification:** [e.g., confirmed 2,930 rows]

## Prompt 2 – October 15, 2026, 7:00 AM session
**Prompt:** Create analysis/analysis.py; remove houses over 4,000 sq ft; print rows removed and remaining.
**Purpose:** Remove the dataset author's recommended outliers.
**Codex produced:** analysis/analysis.py; [rows removed]
**Accepted / Modified / Rejected:** [ ]
**Verification:** [ ]

## Prompt 3 – October 15, 2026, 7:00 AM session
**Prompt:** Extend the script with a regression of SalePrice on Gr Liv Area; print slope, intercept, R²; add residuals.
**Purpose:** One predictor so each residual means "above or below what size predicts."
**Codex produced:** [slope, R²]
**Accepted / Modified / Rejected:** [ ]
**Verification:** [ ]

## Prompt 4 – October 15, 2026, 7:00 AM session
**Prompt:** Neighborhood table (sales, median price, mean residual), excluding neighborhoods under 20 sales, sorted, saved as neighborhood_summary.csv.
**Purpose:** Answer the question directly; small neighborhoods are too noisy.
**Codex produced:** neighborhood_summary.csv; [excluded neighborhoods]
**Accepted / Modified / Rejected:** [ ]
**Verification:** [ ]

## Prompt 5 – October 15, 2026, 7:00 AM session
**Prompt:** Horizontal bar chart of mean residual by neighborhood, zero line, labels, saved as neighborhood_residuals.png.
**Purpose:** Show over- and under-performers at a glance.
**Codex produced:** neighborhood_residuals.png
**Accepted / Modified / Rejected:** [ ]
**Verification:** [chart order matches table?]

## Prompt 6 – October 15, 2026, 7:00 AM session
**Prompt:** Explain a positive mean residual; recompute the NAmes mean residual a second way.
**Purpose:** Independently verify one table value.
**Codex produced:** [both NAmes values; did they match?]
**Accepted / Modified / Rejected:** [ ]
**Verification:** [ ]

## Prompt 7 – October 15, 2026, 7:00 AM session
**Prompt:** Plain-language summary paragraph. Only make claims the table supports.
**Purpose:** Prevent the narrative from claiming causes the analysis didn't test.
**Codex produced:** [summary paragraph]
**Accepted / Modified / Rejected:** [ ]
**Verification:** [ ]
