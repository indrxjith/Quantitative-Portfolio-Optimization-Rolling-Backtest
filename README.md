# 📈 Quantitative Portfolio Optimization & Rolling Backtest

## Overview

Traditional portfolio strategies often suffer from overfitting because they are optimized using historical data and evaluated on the same period. This project implements a realistic quantitative research pipeline that uses rolling walk-forward backtesting to evaluate whether a portfolio optimization strategy can generalize to unseen market conditions.

The system combines Modern Portfolio Theory, Monte Carlo optimization, and advanced risk analytics to construct and evaluate dynamically rebalanced investment portfolios.

---

## Problem Statement

Investors face key questions:

- How should capital be allocated across multiple assets?
- Can an optimized portfolio outperform a market benchmark?
- How does a strategy perform on unseen future data?
- What level of downside risk does the portfolio carry?

This project addresses these challenges using a data-driven portfolio research framework.

---

## Methodology

### 1. Data Collection & Processing
- Download historical market data
- Calculate daily returns
- Clean and prepare financial time-series data

### 2. Portfolio Optimization
- Generate 2,000 Monte Carlo portfolio simulations during each rebalance period
- Estimate expected returns and covariance matrices
- Identify the portfolio with the maximum Sharpe Ratio
- Visualize the Efficient Frontier and risk-return tradeoff

### 3. Rolling Walk-Forward Backtest

To reduce overfitting, the strategy follows a realistic out-of-sample evaluation process:

- Training Window: 5 years of historical data
- Testing Window: 1 year of unseen data
- Rebalancing Frequency: Annual

At each rebalance date:

1. Optimize portfolio weights using only past data
2. Apply the optimized weights to the next year
3. Record real out-of-sample performance
4. Repeat the process throughout the entire dataset

---

## Risk & Performance Analytics

The portfolio is evaluated using:

### Performance Metrics
- Compound Annual Growth Rate (CAGR)
- Annualized Return
- Annualized Volatility
- Sharpe Ratio
- Sortino Ratio

### Downside Risk Metrics
- Maximum Drawdown
- Value at Risk (VaR)
- Conditional Value at Risk (CVaR)

### Benchmark Comparison
- Compare strategy performance against the SPY ETF benchmark

---

## Key Results

The rolling backtest produced:

- 📈 CAGR: **25%+**
- ⚖️ Sharpe Ratio: **~1.0**
- 🛡️ Sortino Ratio: **> 1**
- 📊 Consistent outperformance compared to the SPY benchmark

---

## Technology Stack

### Programming & Data Analysis
- Python
- Pandas
- NumPy

### Quantitative Finance
- Modern Portfolio Theory (MPT)
- Monte Carlo Simulation
- Efficient Frontier Analysis
- Portfolio Optimization
- Risk Management

### Visualization & Analysis
- Matplotlib
- Seaborn

---

## Project Structure

```
quantitative-portfolio-optimization/
│
├── src/
│   ├── rolling_backtest.py
│   ├── optimization.py
│   └── risk_metrics.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── outputs/
│
├── requirements.txt
└── README.md
```

---

## Installation & Usage

Clone the repository:

```bash
git clone <repository-url>
cd quantitative-portfolio-optimization
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the rolling backtest:

```bash
python src/rolling_backtest.py
```

Generate risk analytics:

```bash
python src/risk_metrics.py
```

---

## Future Improvements

Potential extensions:

- Include additional asset classes such as bonds and commodities
- Implement alternative optimization techniques
- Add transaction cost and slippage sensitivity analysis
- Develop an interactive Streamlit dashboard
- Incorporate factor-based portfolio strategies

---

## Author

**Indrajith**

B.Sc Mathematics | Quantitative Finance & Financial Data Analytics
