import streamlit as st
import yfinance as yf
import pandas as pd

def format_number(n):
    if n is None:
        return "N/A"

    n = float(n)

    for unit in ["", "K", "M", "B", "T"]:
        if abs(n) < 1000:
            return f"{n:,.2f}{unit}" if unit else f"{n:,.0f}"
        n /= 1000

    return f"{n:,.2f}P"  # fallback if insanely large

st.title("Stock KPI Lookup")

ticker = st.text_input("Enter ticker", "AAPL").upper().strip()

if ticker:
    stock = yf.Ticker(ticker)
    fast = stock.fast_info

    price = fast.get("lastPrice")
    market_cap = float(fast.get("marketCap"))
    previous_close = fast.get("previousClose")
    day_high = fast.get("dayHigh")
    day_low = fast.get("dayLow")
    volume = fast.get("lastVolume")

    st.subheader(ticker)

    col1, col2, col3 = st.columns(3)

    col1.metric("Current Price", f"${price:,.2f}" if price else "N/A")
    col2.metric("Market Cap", f"${format_number(market_cap)}")
    col3.metric("Previous Close", f"${previous_close:,.2f}" if previous_close else "N/A")

    col4, col5, col6 = st.columns(3)

    col4.metric("Day High", f"${day_high:,.2f}" if day_high else "N/A")
    col5.metric("Day Low", f"${day_low:,.2f}" if day_low else "N/A")
    col6.metric("Last Volume", f"{volume:,.0f}" if volume else "N/A")