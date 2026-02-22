import pandas as pd
import os

raw_path = "../data/raw"
processed_path = "../data/processed"

os.makedirs(processed_path, exist_ok=True)

for file in os.listdir(raw_path):
    if file.endswith(".csv"):

        print("Processing:", file)

        df = pd.read_csv(os.path.join(raw_path, file))

        # sort by date
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values("Date")

        # calculate simple return
        df["Return"] = df["Close"].pct_change()

        # remove first empty row
        df = df.dropna()

        # keep only date and return
        df = df[["Date", "Return"]]

        # save new file
        name = file.replace(".csv", "_returns.csv")
        df.to_csv(os.path.join(processed_path, name), index=False)

print("Done.")