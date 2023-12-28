import pandas as pd
import requests
from datetime import datetime, timedelta

# Tiingo API token
TIINGO_API_TOKEN = '572ec329dc02c59f0d3ac6455cfd4b349570b540'

# Load tickers
tickers_df = pd.read_csv('eod-delta-data.csv')
tickers = tickers_df['ticker'].unique()  # Assuming there's a 'ticker' column

# Load your existing data
df = pd.read_csv('your_file.csv', parse_dates=['date'])  # Adjust the date column name if needed

# Function to fetch data from Tiingo
def fetch_data(ticker, start_date):
    url = f"https://api.tiingo.com/tiingo/daily/{ticker}/prices?startDate={start_date}&token={TIINGO_API_TOKEN}"
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        return pd.DataFrame()  # Empty DataFrame if the request fails

# Update data for each ticker
for ticker in tickers:
    ticker_data = df[df['ticker'] == ticker]  # Filter data for the current ticker
    last_date = ticker_data['date'].max()
    today = datetime.now().date()
    if last_date.date() < today:
        start_date = (last_date + timedelta(days=1)).strftime('%Y-%m-%d')
        new_data = fetch_data(ticker, start_date)
        if not new_data.empty:
            df = pd.concat([df, new_data], ignore_index=True)

# Save the updated DataFrame to CSV
df.to_csv('your_updated_file.csv', index=False)
