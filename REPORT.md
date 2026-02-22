# Quantitative Portfolio Optimization & Rolling Backtest

## 📌 Objective
Develop a systematic portfolio optimization engine that maximizes risk-adjusted returns while eliminating look-ahead bias through rolling out-of-sample testing.

---

## 🧠 Methodology

### Data
- Source: Yahoo Finance
- Frequency: Monthly
- Assets: AAPL, MSFT, SPY
- Time Period: 2000–2025

### Optimization Approach
- Monte Carlo simulation (2000 random portfolios)
- Objective: Maximize Sharpe Ratio
- Rebalancing: Annual
- Rolling Window: 5-year training, 1-year out-of-sample test

### Risk Evaluation
- Volatility
- Sharpe Ratio
- Sortino Ratio
- Maximum Drawdown
- Value at Risk (VaR)
- Conditional VaR (CVaR)
- Rolling Sharpe Analysis

---

## 📊 Results

### Rolling Out-of-Sample Performance
- CAGR: 25.14%
- Volatility: 24.61%
- Sharpe Ratio: 1.02
- Sortino Ratio: 1.23
- VaR (95%): -9.12%
- CVaR (95%): -12.85%

### Benchmark Comparison
Outperformed SPY on both absolute return and risk-adjusted metrics.

---

## 🔍 Key Insights

- Rolling optimization significantly improves Sharpe ratio versus static allocation.
- Risk-adjusted performance remains stable across market regimes.
- Out-of-sample testing removes overfitting bias.

---

## 📈 Visualizations

- Efficient Frontier
- Rolling Portfolio Growth
- Drawdown Analysis
- Benchmark Comparison
- Rolling Sharpe Ratio

---

## 🚀 Conclusion

This project simulates realistic portfolio management by incorporating rolling optimization, risk diagnostics, and benchmark evaluation. The framework can be extended to include multi-factor models, regime detection, or machine learning alpha signals.