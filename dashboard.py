import streamlit as st
import pandas as pd
import numpy as np
import os

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Quantitative Portfolio Dashboard",
    layout="wide"
)

st.title("📊 Quantitative Portfolio Optimization Dashboard")

# -------------------------
# Charts Section
# -------------------------
st.markdown("## 📈 Portfolio Growth")
if os.path.exists("data/outputs/rolling_backtest.png"):
    st.image("data/outputs/rolling_backtest.png", width="stretch")
else:
    st.warning("Rolling growth chart not found.")

st.markdown("## 📉 Drawdown")
if os.path.exists("data/outputs/drawdown.png"):
    st.image("data/outputs/drawdown.png", width="stretch")
else:
    st.warning("Drawdown chart not found.")

st.markdown("## 📊 Efficient Frontier")
if os.path.exists("data/outputs/efficient_frontier.png"):
    st.image("data/outputs/efficient_frontier.png", width="stretch")
else:
    st.warning("Efficient frontier chart not found.")

st.markdown("## 📈 Rolling Sharpe Ratio")
if os.path.exists("data/outputs/rolling_sharpe.png"):
    st.image("data/outputs/rolling_sharpe.png", width="stretch")
else:
    st.warning("Rolling Sharpe chart not found.")

# -------------------------
# Risk & Performance Summary
# -------------------------
st.markdown("---")
st.markdown("## 📊 Risk & Performance Summary")

returns_path = "data/processed/rolling_portfolio_returns.csv"

if os.path.exists(returns_path):

    returns = pd.read_csv(returns_path, index_col=0, parse_dates=True)
    returns = returns.squeeze()

    initial_investment = 100000
    growth = (1 + returns).cumprod() * initial_investment

    years = len(returns) / 12
    cagr = (growth.iloc[-1] / initial_investment) ** (1 / years) - 1
    vol = returns.std() * np.sqrt(12)
    sharpe = cagr / vol

    # Max Drawdown
    rolling_max = growth.cummax()
    drawdown = growth / rolling_max - 1
    max_dd = drawdown.min()

    # Sortino
    downside = returns[returns < 0]
    downside_std = downside.std() * np.sqrt(12)
    sortino = cagr / downside_std if downside_std != 0 else np.nan

    # VaR & CVaR
    var_95 = returns.quantile(0.05)
    cvar_95 = returns[returns <= var_95].mean()

    col1, col2, col3 = st.columns(3)

    col1.metric("CAGR", f"{cagr:.2%}")
    col1.metric("Max Drawdown", f"{max_dd:.2%}")

    col2.metric("Annual Volatility", f"{vol:.2%}")
    col2.metric("Sharpe Ratio", f"{sharpe:.2f}")

    col3.metric("Sortino Ratio", f"{sortino:.2f}")
    col3.metric("VaR (95%)", f"{var_95:.2%}")

    st.metric("CVaR (95%)", f"{cvar_95:.2%}")

else:
    st.error("Rolling portfolio returns file not found. Run rolling_backtest.py first.")