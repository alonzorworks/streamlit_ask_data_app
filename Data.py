# get data from API

import tiingo
from tiingo import TiingoClient
from datetime import date, timedelta




# function t fetch data
def getData(asset):
    # Configuration dictionary for the client
    config = {
        "api_key": "572ec329dc02c59f0d3ac6455cfd4b349570b540",  # Replace with your actual API key
        "session": True  # Optional for performance optimization
    }

    # Create the TiingoClient using the configuration dictionary
    client = TiingoClient(config)

    # Get today's date
    today = date.today()

    # Calculate 6 months back from today
    six_months_ago = today - timedelta(days=365 // 2)


    if asset == 'NASDAQ':
        # Download NASDAQ data
        nasdaq_data = client.get_dataframe(
            "ZYXI", frequency="daily", startDate=six_months_ago, endDate=today
        )

        # # Save data to CSV file
        # file_path = "data/NASDAQ_data.csv"
        # nasdaq_data.to_csv(file_path)
        return nasdaq_data
    elif asset == 'NYSE':
        # Download NYSE data
        nyse_data = client.get_dataframe(
            "ZVIA", frequency="daily", startDate=six_months_ago, endDate=today
        )

        # # Save data to CSV file
        # file_path = "data/NYSE_data.csv"
        # nasdaq_data.to_csv(file_path)
        return nyse_data
    elif asset == 'NYSE ARCA':
        # Download NYSE ARCA data
        nyseARCA_data = client.get_dataframe(
            "ZVIA", frequency="daily", startDate=six_months_ago, endDate=today
        )

        # # Save data to CSV file
        # file_path = "data/NYSE_data.csv"
        # nasdaq_data.to_csv(file_path)
        return nyseARCA_data
    elif asset == 'NYSE MKT':
        # Download NYSE MKT data
        nyseMKT_data = client.get_dataframe(
            "ZDGE", frequency="daily", startDate=six_months_ago, endDate=today
        )

        # # Save data to CSV file
        # file_path = "data/NYSE_data.csv"
        # nasdaq_data.to_csv(file_path)
        return nyseMKT_data
    elif asset == 'NYSE NAT':
        # Download NYSE MKT data
        nyseNAT_data = client.get_dataframe(
            "BRW", frequency="daily", startDate=six_months_ago, endDate=today
        )

        # # Save data to CSV file
        # file_path = "data/NYSE_data.csv"
        # nasdaq_data.to_csv(file_path)
        return nyseNAT_data
    else:
        pass