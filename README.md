# Quantitative Portfolio Optimization & Rolling Backtest

## Overview
This project implements a full quantitative portfolio research pipeline including:

- Data download
- Return calculation
- Covariance & correlation analysis
- Monte Carlo portfolio optimization
- Efficient Frontier visualization
- Rolling out-of-sample backtest
- Risk metrics (Sharpe, Sortino, VaR, CVaR)
- Benchmark comparison

## Methodology
- Optimization Objective: Maximize Sharpe Ratio
- Rolling Window: 5-year training, 1-year test
- Rebalancing: Annual
- Monte Carlo Simulations: 2000 per rebalance

## Key Results
- Rolling CAGR: 25%+
- Rolling Sharpe: ~1.0
- Sortino Ratio: > 1
- Outperformance vs SPY benchmark

## Structure
src/ → Research code  
data/raw/ → Raw downloaded data  
data/processed/ → Processed returns  
data/outputs/ → Charts & results  

## How To Run
pip install -r requirements.txt  
python src/rolling_backtest.py  
python src/risk_metrics.py  

---

Author: Indrajith  