import pandas as pd

# Load merged returns
df = pd.read_csv("../data/merged_returns.csv")

# Remove Date column
returns = df.drop(columns=["Date"])

# Calculate covariance matrix
cov_matrix = returns.cov()

# Save it
cov_matrix.to_csv("../data/covariance_matrix.csv")

print("Covariance matrix created.")