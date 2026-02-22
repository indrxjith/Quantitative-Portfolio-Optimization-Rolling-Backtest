import yfinance as yf
import pandas as pd
import os

TICKERS = ["AAPL", "MSFT", "SPY"]

START_DATE = "2000-01-01"
INTERVAL = "1mo"

DATA_PATH = "../data/raw"
os.makedirs(DATA_PATH, exist_ok=True)

for ticker in TICKERS:
    print(f"Downloading {ticker}...")

    df = yf.download(
        ticker,
        start=START_DATE,
        interval=INTERVAL,
        auto_adjust=True,
        progress=False
    )

    # Force remove multi-index properly
    df.columns = df.columns.map(lambda x: x[0] if isinstance(x, tuple) else x)

    df.reset_index(inplace=True)

    # Keep only necessary columns
    df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]

    file_path = os.path.join(DATA_PATH, f"{ticker}.csv")
    df.to_csv(file_path, index=False)

    print(f"Saved {ticker}")

print("Done.")