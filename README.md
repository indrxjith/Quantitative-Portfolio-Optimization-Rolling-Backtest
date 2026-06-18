# 📈 Quantitative Portfolio Optimization & Rolling Backtest

## Overview

Traditional portfolio optimization methods often suffer from overfitting because they are optimized and evaluated using the same historical data. This project implements a realistic quantitative research pipeline that uses rolling walk-forward backtesting to evaluate whether portfolio optimization strategies can generalize to unseen market conditions.

The project combines Modern Portfolio Theory (MPT), Monte Carlo optimization, risk analytics, benchmark comparison, and interactive visualization to build a complete quantitative portfolio research engine.

---

# Problem Statement

Investors and portfolio managers face several critical questions:

- How should capital be allocated across multiple assets?
- Can an optimized portfolio outperform a passive market benchmark?
- How does a strategy perform in unseen future market environments?
- What is the downside risk during adverse market conditions?

This project addresses these questions using a data-driven quantitative investment framework.

---

# Features

## Data Pipeline
- Automatic historical market data collection
- Data cleaning and preprocessing
- Daily return calculation
- Merging multi-asset return datasets

## Portfolio Research
- Expected return estimation
- Covariance matrix calculation
- Correlation analysis
- Efficient Frontier visualization
- Monte Carlo portfolio optimization
- Maximum Sharpe Ratio portfolio selection

## Walk-Forward Backtesting

To reduce overfitting, the strategy follows an out-of-sample evaluation process:

- Training Window: 5 years
- Testing Window: 1 year
- Rebalancing Frequency: Annual
- Portfolio Simulations: 2,000 Monte Carlo portfolios per rebalance period

At each rebalance step:

1. Historical data is used to find the optimal portfolio weights.
2. The optimized portfolio is applied to the next unseen test period.
3. Portfolio performance is recorded.
4. The process repeats across the complete historical dataset.

---

# Risk & Performance Analysis

The portfolio is evaluated using advanced quantitative metrics:

### Return Metrics
- Compound Annual Growth Rate (CAGR)
- Annualized Returns

### Risk Metrics
- Annualized Volatility
- Maximum Drawdown
- Value at Risk (VaR)
- Conditional Value at Risk (CVaR)

### Risk-Adjusted Performance
- Sharpe Ratio
- Sortino Ratio

### Benchmark Analysis
- Performance comparison against the SPY ETF benchmark

---

# Interactive Dashboard

The project includes a dashboard application for visualizing:

- Portfolio performance over time
- Rolling backtest results
- Risk and return metrics
- Benchmark comparison
- Portfolio analytics

---

# Project Results

The rolling out-of-sample backtest achieved:

| Metric | Result |
|---|---|
| CAGR | 25%+ |
| Sharpe Ratio | ~1.0 |
| Sortino Ratio | > 1 |
| Benchmark | Outperformed SPY |

---

# Project Structure

```
Quantitative-Portfolio-Optimization-Rolling-Backtest/
│
├── data/
│   ├── raw/                 # Raw downloaded historical market data
│   ├── processed/           # Cleaned return datasets
│   └── outputs/             # Charts, visualizations, and generated results
│
├── src/
│   ├── download_data.py     # Market data acquisition
│   ├── calculate_returns.py # Daily return calculation
│   ├── merge_returns.py     # Combining asset return series
│   ├── covariance.py        # Covariance matrix analysis
│   ├── correlation.py       # Correlation analysis
│   ├── optimizer.py         # Monte Carlo portfolio optimization
│   ├── portfolio.py         # Portfolio construction logic
│   ├── backtest.py          # Portfolio backtesting engine
│   ├── rolling_backtest.py  # Walk-forward out-of-sample testing
│   └── risk_metrics.py      # Risk analytics (Sharpe, Sortino, VaR, CVaR)
│
├── dashboard.py             # Interactive dashboard
├── REPORT.md                # Detailed project report
├── requirements.txt         # Python dependencies
├── README.md
└── .gitignore
```

---

# Technology Stack

## Programming
- Python

## Data Analysis
- Pandas
- NumPy

## Visualization
- Matplotlib
- Streamlit Dashboard

## Quantitative Finance
- Modern Portfolio Theory (MPT)
- Efficient Frontier
- Monte Carlo Simulation
- Portfolio Optimization
- Rolling Walk-Forward Backtesting
- Risk Management

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Quantitative-Portfolio-Optimization-Rolling-Backtest.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Usage

Run the complete rolling backtest:

```bash
python src/rolling_backtest.py
```

Calculate advanced risk metrics:

```bash
python src/risk_metrics.py
```

Launch the interactive dashboard:

```bash
streamlit run dashboard.py
```

---

# Future Improvements

Potential future enhancements include:

- Multi-asset portfolio support (bonds, commodities, ETFs)
- Alternative optimization techniques
- Factor-based investing strategies
- More realistic transaction cost modeling
- Advanced machine learning-based portfolio allocation

---

# Author

## Indrajith

B.Sc Mathematics  
Financial Data Analytics | Quantitative Finance Enthusiast
