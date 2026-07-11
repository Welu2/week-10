# Task 1: Analysis Plan

# 1. Data Analysis Workflow

The planned workflow consists of:

1. Load Brent oil price data
2. Clean missing values
3. Convert dates
4. Perform exploratory analysis
5. Analyze trend
6. Test stationarity using ADF
7. Analyze volatility
8. Compile external geopolitical events
9. Apply Change Point Detection
10. Interpret structural breaks
11. Compare breaks against historical events
12. Produce visualizations
13. Communicate findings

---

# Event Dataset

A structured CSV containing important oil market events has been created.

---

# Assumptions

- Daily Brent price accurately reflects market conditions.
- Event dates are approximate.
- Multiple events may overlap.
- Market reaction may lag event occurrence.

---

# Limitations

- Correlation does not imply causation.
- Some events may have delayed effects.
- Global markets respond to multiple simultaneous factors.
- Data quality depends on source reliability.

---

# Time Series Properties

## Trend

Oil prices exhibit long-term upward and downward cycles.

## Stationarity

Raw prices are expected to be non-stationary.

ADF testing will verify stationarity.

Differencing may be required.

## Volatility

Oil markets exhibit volatility clustering.

Periods of crises often show increased variance.

---

# Why Change Point Models?

Change point models identify dates where the statistical properties of the price series change significantly.

Examples include:

- Gulf War
- Financial Crisis
- COVID-19
- Russia-Ukraine conflict

---

# Expected Outputs

The model should estimate:

- Break dates
- Mean changes
- Variance changes
- Confidence around break locations

---

# Communication Channels

Results will be communicated through:

- Technical report
- Interactive notebook
- Power BI/Tableau dashboard
- Executive presentation
- GitHub repository