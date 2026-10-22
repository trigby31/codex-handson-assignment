"""
Ames Housing: Neighborhood performance after controlling for size.

Question: After accounting for above-ground living area, which Ames
neighborhoods sell for more or less than expected, and by how much?

Run from the repository root:  python analysis/analysis.py
"""
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "analysis"

# --- 1. Load ---------------------------------------------------------------
data_file = next(
    (ROOT / name for name in ["AmesHousing.csv", "AmesHousing-1.csv"]
     if (ROOT / name).exists()),
    None,
)
if data_file is None:
    raise FileNotFoundError("Put AmesHousing.csv in the repository root.")

df = pd.read_csv(data_file)
cols = ["SalePrice", "Gr Liv Area", "Neighborhood"]
print(f"Loaded {data_file.name}: {df.shape[0]} rows, {df.shape[1]} columns")
print("Missing values in key columns:")
print(df[cols].isna().sum().to_string(), "\n")

# --- 2. Clean: remove the very large houses the dataset author flags --------
before = len(df)
df = df[df["Gr Liv Area"] <= 4000].copy()
print(f"Removed {before - len(df)} houses over 4,000 sq ft; {len(df)} remain\n")

# --- 3. Regression: SalePrice on Gr Liv Area --------------------------------
x = df["Gr Liv Area"].to_numpy(dtype=float)
y = df["SalePrice"].to_numpy(dtype=float)
slope, intercept = np.polyfit(x, y, 1)
pred = intercept + slope * x
r2 = 1 - ((y - pred) ** 2).sum() / ((y - y.mean()) ** 2).sum()
df["Residual"] = y - pred
print(f"Slope: ${slope:,.2f} per sq ft")
print(f"Intercept: ${intercept:,.0f}")
print(f"R-squared: {r2:.3f}\n")

# --- 4. Neighborhood summary table ------------------------------------------
summary = (
    df.groupby("Neighborhood")
    .agg(Sales=("SalePrice", "size"),
         MedianPrice=("SalePrice", "median"),
         MeanResidual=("Residual", "mean"))
)
excluded = summary[summary["Sales"] < 20].index.tolist()
summary = (summary[summary["Sales"] >= 20]
           .sort_values("MeanResidual", ascending=False)
           .round({"MedianPrice": 0, "MeanResidual": 0}))
print(f"Excluded (fewer than 20 sales): {', '.join(excluded)}\n")
print(summary.to_string(), "\n")
summary.to_csv(OUT / "neighborhood_summary.csv")

# --- 5. Check: recompute one value a second way -----------------------------
names = df[df["Neighborhood"] == "NAmes"]
check = (names["SalePrice"] - (intercept + slope * names["Gr Liv Area"])).mean()
print(f"NAmes mean residual, table: {summary.loc['NAmes', 'MeanResidual']:,.0f}; "
      f"recomputed: {check:,.0f}\n")

# --- 6. Chart ----------------------------------------------------------------
plot = summary.iloc[::-1]  # highest at top
colors = ["#2b7a78" if v >= 0 else "#c0392b" for v in plot["MeanResidual"]]
fig, ax = plt.subplots(figsize=(8, 9))
ax.barh(plot.index, plot["MeanResidual"], color=colors)
ax.axvline(0, color="black", linewidth=1)
ax.set_xlabel("Mean residual ($): actual price minus price predicted by living area")
ax.set_ylabel("Neighborhood")
ax.set_title("Ames neighborhoods: selling above or below what size predicts")
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"-${-v:,.0f}" if v < 0 else f"${v:,.0f}"))
fig.tight_layout()
fig.savefig(OUT / "neighborhood_residuals.png", dpi=150)
print("Saved analysis/neighborhood_summary.csv and analysis/neighborhood_residuals.png")
