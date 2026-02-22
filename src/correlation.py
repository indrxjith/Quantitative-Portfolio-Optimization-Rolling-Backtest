import pandas as pd

# Load merged returns
df = pd.read_csv("../data/merged_returns.csv")

# Remove Date column
returns = df.drop(columns=["Date"])

# Calculate correlation matrix
corr_matrix = returns.corr()

# Save it
corr_matrix.to_csv("../data/correlation_matrix.csv")

print("Correlation matrix created.")