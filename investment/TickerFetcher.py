import requests
import pandas as pd


def fetch_us_tickers():
    url = "https://api.nasdaq.com/api/screener/stocks?tableonly=false&limit=10000&download=true"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # Make the API request
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parse the JSON response
        data = response.json()
        rows = data["data"]["rows"]  # Access the rows containing stock details

        # Extract ticker symbols
        tickers = [row["symbol"] for row in rows]

        return tickers
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []


# Fetch tickers
tickers = fetch_us_tickers()

if tickers:
    print(f"Fetched {len(tickers)} tickers:")
    print(tickers)  # Display ticker symbols

    # Save to CSV
    df = pd.DataFrame(tickers, columns=["Ticker"])
    df.to_csv("us_tickers.csv", index=False)
    print("Tickers saved to 'us_tickers.csv'.")
else:
    print("No tickers fetched.")
