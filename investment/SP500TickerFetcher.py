import yfinance as yf


def get_sp500_tickers():
    # Fetch the S&P 500 index from Yahoo Finance
    sp500 = yf.Ticker("^GSPC")

    # Fetch the list of components (tickers) in the S&P 500
    tickers = sp500.history(period="1d")

    return tickers


# Fetch the tickers
tickers = get_sp500_tickers()

if not tickers.empty:
    print(f"Fetched {len(tickers)} tickers.")
else:
    print("No tickers fetched.")
