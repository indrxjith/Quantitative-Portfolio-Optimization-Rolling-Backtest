import pandas as pd
import numpy as np

# Load data
returns = pd.read_csv("../data/merged_returns.csv")
returns = returns.drop(columns=["Date"])

# Equal weights
weights = np.array([1/3, 1/3, 1/3])

# Mean returns
mean_returns = returns.mean()

# Covariance matrix
cov_matrix = returns.cov()

# Expected portfolio return
portfolio_return = np.dot(weights, mean_returns)

# Portfolio volatility
portfolio_volatility = np.sqrt(
    np.dot(weights.T, np.dot(cov_matrix, weights))
)

print("Expected Monthly Return:", portfolio_return)
print("Monthly Volatility:", portfolio_volatility)

# Annualized return
annual_return = portfolio_return * 12

# Annualized volatility
annual_volatility = portfolio_volatility * np.sqrt(12)

print("Annual Return:", annual_return)
print("Annual Volatility:", annual_volatility)

# Risk-free rate (assume 0 for now)
risk_free_rate = 0

sharpe_ratio = (annual_return - risk_free_rate) / annual_volatility

print("Sharpe Ratio:", sharpe_ratio)