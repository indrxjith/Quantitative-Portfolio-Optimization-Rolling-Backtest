import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load returns
returns = pd.read_csv("../data/merged_returns.csv")
returns["Date"] = pd.to_datetime(returns["Date"])
returns.set_index("Date", inplace=True)

# Load optimal weights
weights_df = pd.read_csv("../data/optimal_weights.csv")
weights = weights_df["Max_Sharpe_Weight"].values

# Portfolio returns
portfolio_returns = returns.dot(weights)

# SPY benchmark (assumes SPY column exists)
spy_returns = returns["SPY"]

# Initial investment
initial_investment = 100000

# Portfolio growth
portfolio_growth = (1 + portfolio_returns).cumprod() * initial_investment

# SPY growth
spy_growth = (1 + spy_returns).cumprod() * initial_investment

# CAGR function
def calculate_cagr(series):
    years = len(series) / 12
    return (series.iloc[-1] / series.iloc[0]) ** (1 / years) - 1

portfolio_cagr = calculate_cagr(portfolio_growth)
spy_cagr = calculate_cagr(spy_growth)

# Volatility
portfolio_vol = portfolio_returns.std() * np.sqrt(12)
spy_vol = spy_returns.std() * np.sqrt(12)

# Sharpe
portfolio_sharpe = portfolio_cagr / portfolio_vol
spy_sharpe = spy_cagr / spy_vol

# Plot comparison
plt.figure(figsize=(10,6))
plt.plot(portfolio_growth, label="Optimized Portfolio")
plt.plot(spy_growth, label="SPY Benchmark")
plt.title("Portfolio vs SPY Growth")
plt.legend()
plt.savefig("../data/benchmark_comparison.png", dpi=300)
plt.close()

print("\n===== Benchmark Comparison =====")
print(f"Portfolio CAGR: {portfolio_cagr:.2%}")
print(f"SPY CAGR: {spy_cagr:.2%}")
print(f"Portfolio Sharpe: {portfolio_sharpe:.2f}")
print(f"SPY Sharpe: {spy_sharpe:.2f}")