import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load rolling portfolio returns
returns = pd.read_csv("../data/merged_returns.csv")
returns["Date"] = pd.to_datetime(returns["Date"])
returns.set_index("Date", inplace=True)

# Use optimized weights from rolling backtest
# (You can later load dynamic weights if needed)

portfolio = returns.mean(axis=1)  # placeholder simple aggregation

# Downside deviation
downside = portfolio[portfolio < 0]
sortino = (portfolio.mean() * 12) / (downside.std() * np.sqrt(12))

# VaR (95%)
var_95 = np.percentile(portfolio, 5)

# CVaR (Expected Shortfall)
cvar_95 = portfolio[portfolio <= var_95].mean()

print("\n===== Risk Metrics =====")
print(f"Sortino Ratio: {sortino:.2f}")
print(f"Value at Risk (95%): {var_95:.2%}")
print(f"Conditional VaR (95%): {cvar_95:.2%}")

# Rolling Sharpe
rolling_sharpe = (
    portfolio.rolling(12).mean() * 12
) / (portfolio.rolling(12).std() * np.sqrt(12))

plt.figure(figsize=(10,6))
plt.plot(rolling_sharpe)
plt.title("Rolling 12-Month Sharpe Ratio")
plt.savefig("../data/rolling_sharpe.png", dpi=300)
plt.close()
