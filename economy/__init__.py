import requests
import pandas as pd

# URL to fetch the JSON
url = "https://www.imf.org/external/datamapper/api/v1/indicators"  # Replace with the actual API URL

# Base URL for the second API
base_url = "https://www.imf.org/external/datamapper/api/v1"

try:
    # Send GET request
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the JSON response
    data = response.json()

    # Extract indicator labels and keys
    indicators = data["indicators"]

    # Fetch details for each indicator
    for key, details in indicators.items():
        if key=="NGDP_RPCH" or key=="rgc" or key=="NGDP_R_PCH" or key=="NGDPXO_RPCH" or key=="NGDPRPC_PCH":
            label = details["label"]  # Get the label
            detail_url = f"{base_url}/{key}/USA/CHN/IND?periods=2023,2024,2025"  # Modify URL as needed
            detail_response = requests.get(detail_url)

            if detail_response.status_code == 200:
                detail_data = detail_response.json()

                # Extract 'values' from the detail_data
                values = detail_data.get("values", {}).get(key, {})
                if values:
                    table_data = []
                    for country, country_data in values.items():
                        for year, value in country_data.items():
                            table_data.append({"Country": country, "Year": int(year), "Value": value})

                    # Convert to DataFrame
                    if table_data:  # Ensure there is data to process
                        df = pd.DataFrame(table_data)
                        #print("\nRaw DataFrame:")
                        #print(df)  # Debug: Print the raw DataFrame to verify structure

                        # Pivot for better display
                        df = df.pivot(index="Year", columns="Country", values="Value")

                        # Print the label and table
                        print(f"\nIndicator: {label}")
                        print(df)
                    else:
                        print(f"No data available for indicator: {label}")
                else:
                    print(f"No data available for indicator: {label}")
            else:
                print(f"Failed to fetch details for {label}: {detail_response.status_code}")

except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
