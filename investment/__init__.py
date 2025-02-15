import yfinance as yf
from tabulate import tabulate

def fetch_stock_data(ticker):
    """
    Fetch balance sheet, financials, earnings history, and cashflow data for a given ticker symbol.
    """
    stock = yf.Ticker(ticker)
    balance_sheet = stock.balance_sheet
    financials = stock.financials
    earnings_history = stock.earnings_history
    cashflow = stock.cashflow

    # Extract all available balance sheet data
    balance_sheet_data = {}
    for row in balance_sheet.index:
        balance_sheet_data[row] = balance_sheet.loc[row].to_dict()

    # Extract all available financials data
    financial_data = {}
    for row in financials.index:
        financial_data[row] = financials.loc[row].to_dict()

    # Extract all available earnings history data (check type before processing)
    earnings_data = []
    for earnings in earnings_history:
        if isinstance(earnings, dict):
            earnings_data.append(earnings)
        else:
            # If earnings is not a dictionary, append a default dict with empty data
            earnings_data.append({
                "date": "N/A",
                "epsActual": "N/A",
                "epsEstimate": "N/A",
                "surprisePercentage": "N/A"
            })

    # Extract all available cashflow data
    cashflow_data = {}
    for row in cashflow.index:
        cashflow_data[row] = cashflow.loc[row].to_dict()

    return balance_sheet_data, financial_data, earnings_data, cashflow_data

def print_table(data, headers, title):
    """
    Print data in a tabular format with a title.
    """
    rows = []
    dates = set()
    for key in data:
        dates.update(data[key].keys())

    # Add rows for each date
    for date in sorted(dates):
        row = [date]
        for field in data:
            row.append(data[field].get(date, "N/A"))
        rows.append(row)

    print(f"{title} Data:")
    print(tabulate(rows, headers=headers, tablefmt="grid"))
    print("\n")

def print_earnings_history_table(earnings_data):
    """
    Print earnings history data in a tabular format.
    """
    earnings_headers = ["Date", "EPS Actual", "EPS Estimate", "Surprise (%)"]

    earnings_rows = []
    for earnings in earnings_data:
        earnings_rows.append([
            earnings.get("date", "N/A"),
            earnings.get("epsActual", "N/A"),
            earnings.get("epsEstimate", "N/A"),
            earnings.get("surprisePercentage", "N/A")
        ])

    print(f"Earnings History Data:")
    print(tabulate(earnings_rows, headers=earnings_headers, tablefmt="grid"))
    print("\n")

# Main program
def main():
    # Prompt user for the ticker symbol
    ticker = input("Enter the ticker symbol of the stock: ").upper()

    # Prompt user for the data fields they want to see
    print("\nEnter the data fields you want to display (comma-separated) or type 'showall' to display everything:")
    print("Example: Net Debt, Total Debt, Basic EPS, Net Income")
    user_fields = input("Fields: ").strip().lower()

    # Fetch the data
    balance_sheet_data, financial_data, earnings_data, cashflow_data = fetch_stock_data(ticker)

    if user_fields == "showall":
        # Print all data
        if balance_sheet_data:
            balance_sheet_headers = ["Date"] + list(balance_sheet_data.keys())
            print_table(balance_sheet_data, balance_sheet_headers, "Balance Sheet")

        if financial_data:
            financial_headers = ["Date"] + list(financial_data.keys())
            print_table(financial_data, financial_headers, "Financials")

        if earnings_data:
            print_earnings_history_table(earnings_data)  # Print earnings history in a separate table

        if cashflow_data:
            cashflow_headers = ["Date"] + list(cashflow_data.keys())
            print_table(cashflow_data, cashflow_headers, "Cashflow")
    else:
        # Process user-defined fields
        user_fields_list = [field.strip() for field in user_fields.split(",")]

        def filter_data(data):
            filtered_data = {}
            for key, values in data.items():
                if key.lower() in user_fields_list:
                    filtered_data[key] = values
            return filtered_data

        # Filter data for the first ticker
        filtered_balance_sheet = filter_data(balance_sheet_data)
        filtered_financials = filter_data(financial_data)

        if filtered_balance_sheet or filtered_financials:
            compare = input("Do you want to compare this data with another ticker? (yes/no): ").strip().lower()
            if compare == "yes":
                second_ticker = input("Enter the second ticker symbol: ").upper()
                second_balance_sheet, second_financials, _, _ = fetch_stock_data(second_ticker)

                # Get available dates for comparison
                available_dates = set()
                for data in [filtered_balance_sheet, second_balance_sheet, filtered_financials, second_financials]:
                    for key in data:
                        available_dates.update(data[key].keys())

                available_dates = sorted(available_dates)
                print("Available dates for comparison:")
                for i, date in enumerate(available_dates):
                    print(f"{i + 1}: {date}")

                date_index = int(input("Select a date by number: ")) - 1
                if 0 <= date_index < len(available_dates):
                    date_to_compare = available_dates[date_index]

                    # Prepare comparison table
                    comparison_rows = []
                    headers = ["Field", f"{ticker} ({date_to_compare})", f"{second_ticker} ({date_to_compare})"]

                    for field in user_fields_list:
                        row = [field]
                        row.append(filtered_balance_sheet.get(field, {}).get(date_to_compare, "N/A") or filtered_financials.get(field, {}).get(date_to_compare, "N/A"))
                        row.append(second_balance_sheet.get(field, {}).get(date_to_compare, "N/A") or second_financials.get(field, {}).get(date_to_compare, "N/A"))
                        comparison_rows.append(row)

                    print("Comparison Table:")
                    print(tabulate(comparison_rows, headers=headers, tablefmt="grid"))
                else:
                    print("Invalid date selection.")

        if filtered_balance_sheet:
            balance_sheet_headers = ["Date"] + list(filtered_balance_sheet.keys())
            print_table(filtered_balance_sheet, balance_sheet_headers, "Filtered Balance Sheet")

        if filtered_financials:
            financial_headers = ["Date"] + list(filtered_financials.keys())
            print_table(filtered_financials, financial_headers, "Filtered Financials")

        if "eps actual" in user_fields_list or "eps estimate" in user_fields_list or "surprise (%)" in user_fields_list:
            print_earnings_history_table(earnings_data)

if __name__ == "__main__":
    main()
