# Ames Housing: Neighborhood Performance After Controlling for Size

**Analytical question:** After accounting for above-ground living area, which
Ames neighborhoods sell for more or less than expected, and by how much?

**Codex session date:** October 22, 2026

## Summary of Findings
After removing a small number of unusually large houses, I used a linear
regression to estimate how much of a home's sale price is explained by its
above-ground living area. Living area turned out to be a strong predictor:
larger homes consistently sold for more, and size alone accounted for a
substantial share of the differences in price. To see how location fits in,
I compared each house's actual sale price to the price its size predicted,
then averaged those differences by neighborhood, leaving out neighborhoods
with too few sales to give a reliable picture. Some neighborhoods sold well
above what their homes' size would suggest, while others sold noticeably
below it. In plain terms, size explains a lot of a home's price in Ames, but
location still matters: two houses of the same size can sell for very
different amounts depending on where they are. This analysis shows where
those gaps exist, not why; factors like home age, quality, and lot size
likely play a role.

## Repository contents
- `/prompts/` – exported Codex session transcript
- `/log/ai-workflow-log.md` – per-prompt workflow log
- `/analysis/` – script, neighborhood_summary.csv, neighborhood_residuals.png
- `reflection.md` – reflection on directing Codex
