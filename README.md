# Brent Oil Price Change Point Analysis Dashboard

## Project Overview

This project analyzes historical Brent crude oil prices using **Bayesian Change Point Detection** and presents the results through an interactive **Flask + React dashboard**. The goal is to identify structural changes in oil prices and explore how major geopolitical, economic, and OPEC-related events influence market behavior.

---

## Objectives

* Analyze Brent oil price trends over time.
* Detect structural breaks using Bayesian Change Point Modeling (PyMC).
* Associate detected change points with historical events.
* Build an interactive dashboard for exploring prices, events, and model outputs.

---

# Project Structure

```text
week-10/

├── backend/
│   ├── app.py
│   ├── routes.py
│   ├── services.py
│   ├── requirements.txt
│   ├── Data/
│   │   ├── BrentOilPrices.csv
│   │   └── oil_market_events.csv
│   └── analysis/
│       └── change_points.json
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── styles/
│   │   ├── App.jsx
│   │   └── main.jsx
│   └── package.json
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_TimeSeries_Analysis.ipynb
│   ├── 03_Event_Analysis.ipynb
│   └── 04_Bayesian_ChangePoint.ipynb
│
├── scripts/
│   ├── preprocessing.py
│   ├── changepoint.py
│   ├── bayesian_model.py
│   └── utils.py
│
├── tests/
└── README.md
```

---

# Task 2: Bayesian Change Point Modeling

## Objective

Identify structural breaks in Brent oil prices using Bayesian inference and relate them to historical oil market events.

## Workflow

1. Load Brent oil price data.
2. Convert the `Date` column to datetime.
3. Perform exploratory data analysis.
4. Compute log returns.
5. Test stationarity using the Augmented Dickey–Fuller (ADF) test.
6. Analyze rolling volatility.
7. Build a Bayesian change point model in PyMC.
8. Perform MCMC sampling.
9. Evaluate convergence using R-hat diagnostics.
10. Compare detected change points with historical events.

## Bayesian Model

The implemented model includes:

* Discrete Uniform prior for the change point (`tau`)
* Mean before change (`μ₁`)
* Mean after change (`μ₂`)
* Shared standard deviation (`σ`)
* `pm.math.switch()` to model regime changes
* MCMC sampling using `pm.sample()`

## Outputs

* Posterior distribution of the change point
* Posterior estimates for model parameters
* Trace plots
* Convergence diagnostics
* Quantified price changes before and after the detected structural break
* Event comparison analysis

---

# Task 3: Interactive Dashboard

## Objective

Develop a full-stack dashboard that enables stakeholders to explore Brent oil prices, historical events, and Bayesian change point analysis.

---

## Backend (Flask)

Implemented REST API endpoints:

| Endpoint                 | Description                  |
| ------------------------ | ---------------------------- |
| GET `/api/prices`        | Historical Brent oil prices  |
| GET `/api/events`        | Historical oil market events |
| GET `/api/change-points` | Bayesian model output        |
| GET `/api/kpis`          | Dashboard summary metrics    |
| GET `/api/price-range`   | Filter prices by date range  |
| GET `/api/event/<id>`    | Retrieve a specific event    |

### Backend Features

* Historical data loading
* Event dataset integration
* Bayesian results API
* KPI computation
* Date range filtering
* Modular service architecture

---

## Frontend (React + Vite)

The dashboard is built using:

* React
* Vite
* Axios
* Recharts

### Dashboard Components

* KPI Summary Cards
* Historical Brent Oil Price Chart
* Date Range Filter
* Historical Event Timeline
* Bayesian Change Point Results Table

### Features

* Interactive line chart
* Historical event visualization
* Date range filtering
* Bayesian analysis summary
* Responsive layout for desktop and mobile devices

---

# Technologies

## Backend

* Python
* Flask
* Flask-CORS
* Pandas
* NumPy
* PyMC
* ArviZ

## Frontend

* React
* Vite
* Axios
* Recharts

---

# Installation

## Clone the Repository

```bash
git clone <repository-url>
cd week-10
```

---

## Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the backend:

```bash
python app.py
```

The backend runs at:

```text
http://127.0.0.1:5000
```

---

## Frontend Setup

```bash
cd frontend

npm install
```

Run the development server:

```bash
npm run dev
```

The frontend runs at:

```text
http://localhost:5173
```

---

# Running Tests

Execute all tests from the project root:

```bash
pytest
```

---

# Dashboard Preview

The dashboard includes:

* Historical Brent oil price visualization
* Bayesian change point results
* Historical event timeline
* KPI summary cards
* Interactive date filtering

Screenshots of the dashboard can be found in the `screenshots/` directory.

---

# Future Improvements

* Multiple Bayesian change point detection
* Interactive event highlighting on charts
* Drill-down analysis around selected events
* Integration of macroeconomic indicators (GDP, inflation, exchange rates)
* Export dashboard reports to PDF or CSV
* User authentication and saved dashboard views

---
