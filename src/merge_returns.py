import pandas as pd
import os

processed_path = "../data/processed"

merged_df = None

for file in os.listdir(processed_path):

    if file.endswith("_returns.csv"):

        # Extract ticker name
        ticker = file.replace("_returns.csv", "")

        # Read file
        df = pd.read_csv(os.path.join(processed_path, file))

        # Rename Return column to ticker name
        df = df.rename(columns={"Return": ticker})

        if merged_df is None:
            merged_df = df
        else:
            merged_df = pd.merge(merged_df, df, on="Date", how="inner")

# Save final merged file
merged_df.to_csv("../data/merged_returns.csv", index=False)

print("Merged successfully.")