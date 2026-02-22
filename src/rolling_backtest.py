import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load processed returns
returns = pd.read_csv("../data/processed/merged_returns.csv")
returns["Date"] = pd.to_datetime(returns["Date"])
returns.set_index("Date", inplace=True)

window_years = 5
rebalance_years = 1

window_months = window_years * 12
rebalance_months = rebalance_years * 12

transaction_cost = 0.001  # 0.1% cost per rebalance

portfolio_returns = []

for start in range(0, len(returns) - window_months - rebalance_months, rebalance_months):

    # Training window
    train = returns.iloc[start:start + window_months]

    mean_returns = train.mean()
    cov_matrix = train.cov()

    # Monte Carlo optimization
    best_sharpe = -np.inf
    best_weights = None

    for _ in range(2000):

        weights = np.random.random(len(mean_returns))
        weights /= np.sum(weights)

        annual_return = np.dot(weights, mean_returns) * 12
        annual_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 12, weights)))

        sharpe = annual_return / annual_vol

        if sharpe > best_sharpe:
            best_sharpe = sharpe
            best_weights = weights

    # Out-of-sample period
    test = returns.iloc[start + window_months : start + window_months + rebalance_months]

    period_returns = test.dot(best_weights).copy()

    # Apply transaction cost at rebalance
    period_returns.iloc[0] -= transaction_cost

    portfolio_returns.extend(period_returns)

# Convert to Series
portfolio_returns = pd.Series(portfolio_returns)
portfolio_returns.index = returns.index[window_months : window_months + len(portfolio_returns)]

# Growth calculation
initial_investment = 100000
growth = (1 + portfolio_returns).cumprod() * initial_investment

# Save plot
plt.figure(figsize=(10,6))
plt.plot(growth)
plt.title("Rolling Out-of-Sample Portfolio Growth (With Transaction Costs)")
plt.xlabel("Date")
plt.ylabel("Portfolio Value")
plt.savefig("../data/outputs/rolling_backtest.png", dpi=300)
plt.close()

# Performance metrics
years = len(portfolio_returns) / 12
cagr = (growth.iloc[-1] / initial_investment) ** (1 / years) - 1
vol = portfolio_returns.std() * np.sqrt(12)
sharpe = cagr / vol

print("\n===== Rolling Backtest Performance (With Costs) =====")
print(f"CAGR: {cagr:.2%}")
print(f"Volatility: {vol:.2%}")
print(f"Sharpe Ratio: {sharpe:.2f}")