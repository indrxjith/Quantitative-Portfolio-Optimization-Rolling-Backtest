import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Load Data
# -----------------------------

returns = pd.read_csv("../data/merged_returns.csv")
returns = returns.drop(columns=["Date"])

mean_returns = returns.mean()
cov_matrix = returns.cov()

asset_names = returns.columns
num_assets = len(asset_names)

num_portfolios = 5000

results = np.zeros((3, num_portfolios))
weight_list = []

# -----------------------------
# Monte Carlo Simulation
# -----------------------------

for i in range(num_portfolios):

    weights = np.random.random(num_assets)
    weights /= np.sum(weights)

    weight_list.append(weights)

    # Annual return
    portfolio_return = np.dot(weights, mean_returns) * 12

    # Annual volatility
    portfolio_volatility = np.sqrt(
        np.dot(weights.T, np.dot(cov_matrix * 12, weights))
    )

    sharpe_ratio = portfolio_return / portfolio_volatility

    results[0, i] = portfolio_return
    results[1, i] = portfolio_volatility
    results[2, i] = sharpe_ratio

# -----------------------------
# Identify Optimal Portfolios
# -----------------------------

# Maximum Sharpe
max_sharpe_idx = np.argmax(results[2])
max_sharpe_return = results[0, max_sharpe_idx]
max_sharpe_vol = results[1, max_sharpe_idx]
max_sharpe_weights = weight_list[max_sharpe_idx]

# Minimum Volatility
min_vol_idx = np.argmin(results[1])
min_vol_return = results[0, min_vol_idx]
min_vol_vol = results[1, min_vol_idx]
min_vol_weights = weight_list[min_vol_idx]

# -----------------------------
# Print Results Cleanly
# -----------------------------

print("\n===== Maximum Sharpe Portfolio =====")
print(f"Annual Return: {max_sharpe_return:.2%}")
print(f"Annual Volatility: {max_sharpe_vol:.2%}")
print("Weights:")
for name, weight in zip(asset_names, max_sharpe_weights):
    print(f"{name}: {weight:.2%}")

print("\n===== Minimum Volatility Portfolio =====")
print(f"Annual Return: {min_vol_return:.2%}")
print(f"Annual Volatility: {min_vol_vol:.2%}")
print("Weights:")
for name, weight in zip(asset_names, min_vol_weights):
    print(f"{name}: {weight:.2%}")

# -----------------------------
# Save Optimal Weights
# -----------------------------

optimal_df = pd.DataFrame({
    "Asset": asset_names,
    "Max_Sharpe_Weight": max_sharpe_weights,
    "Min_Vol_Weight": min_vol_weights
})

optimal_df.to_csv("../data/optimal_weights.csv", index=False)

print("\nOptimal weights saved to data/optimal_weights.csv")

# -----------------------------
# Plot Efficient Frontier
# -----------------------------

plt.figure(figsize=(10, 6))
plt.scatter(results[1, :], results[0, :], c=results[2, :], cmap='viridis')
plt.colorbar(label='Sharpe Ratio')

plt.scatter(max_sharpe_vol, max_sharpe_return,
            color='red', s=120, label='Max Sharpe')

plt.scatter(min_vol_vol, min_vol_return,
            color='blue', s=120, label='Min Volatility')

plt.xlabel('Volatility')
plt.ylabel('Return')
plt.title('Efficient Frontier')
plt.legend()

plt.savefig("../data/efficient_frontier.png", dpi=300)
plt.close()

print("Efficient frontier saved as data/efficient_frontier.png")