# Lets define all models here

# import libraries
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from statsmodels.tsa.arima.model import ARIMA
from tsai.models.RNN import RNN
from tsai.data.core import TSDataset, TSDataLoaders
from tsai.utils import accuracy
import torch


# Arima model
def arima(data):
    # print(data.head())
    

    # Step 1: Apply ARIMA to predict future values for each hour
    # Example: Assuming you want to predict the next 24 hours of 'Low' and 'High'
    order = (1, 1, 1)  # Example order, you may need to tune this

    # Create an empty DataFrame to store forecasted values for each hour
    forecast_df = pd.DataFrame(index=pd.date_range(start=data.index[-1] + pd.Timedelta(hours=1), periods=24, freq='H'))

    for column in ['low', 'high']:
        model = ARIMA(data[column], order=order)
        fit_model = model.fit()
        future_values = fit_model.forecast(steps=24)  # Forecast for the next 24 hours

        # Calculate the range of low and high values for each hour
        forecast_df[column + '_low'] = data[column].iloc[-1] + np.cumsum(future_values)
        forecast_df[column + '_high'] = data['high'].iloc[-1] + np.cumsum(future_values)

    # Step 3: Plot Candlestick Chart using Plotly
    fig = go.Figure()

    # Plot historical data
    fig.add_trace(go.Candlestick(x=data.index,
                    open=data['open'],
                    high=data['high'],
                    low=data['low'],
                    close=data['close'],
                    name='Historical Data'))

    # Plot forecasted data
    for column in ['low', 'high']:
        fig.add_trace(go.Candlestick(x=forecast_df.index,
                        open=forecast_df[column + '_low'],
                        high=forecast_df[column + '_high'],
                        low=forecast_df[column + '_low'],
                        close=forecast_df[column + '_high'],
                        name=f'Forecasted {column}'))

    # Customize the layout if needed
    fig.update_layout(
        title='Next Day Candlestick Chart with ARIMA Prediction',
        xaxis_title='Next 24 Hours',
        yaxis_title='Price',
    )

    # Show the plot
    # fig.show()
    return fig
