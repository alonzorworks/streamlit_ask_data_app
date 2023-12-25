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

    for column in ['Low', 'High']:
        model = ARIMA(data[column], order=order)
        fit_model = model.fit()
        future_values = fit_model.forecast(steps=24)  # Forecast for the next 24 hours

        # Calculate the range of low and high values for each hour
        forecast_df[column + '_low'] = data[column].iloc[-1] + np.cumsum(future_values)
        forecast_df[column + '_high'] = data['High'].iloc[-1] + np.cumsum(future_values)

    # Step 3: Plot Candlestick Chart using Plotly
    fig = go.Figure()

    # Plot historical data
    fig.add_trace(go.Candlestick(x=data.index,
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'],
                    name='Historical Data'))

    # Plot forecasted data
    for column in ['Low', 'High']:
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


# LSTM from tsai
# def LSTM(data):
#     # Separate features and target
#     features = ["Open", "Low", "Close", "Volume"]  # Adjust feature names
#     target_col = "High"

#     # # Reshape data for time series (assuming observations are columns)
#     # data = data.transpose()

#     # Split into training and validation sets
#     train_df, valid_df = train_test_split(data, test_size=0.2, random_state=42, shuffle=False)
#     train_df = train_df.transpose()
#     valid_df = valid_df.transpose()

#     print(train_df.shape)
#     print(valid_df.shape)

#     # Create TSDataset objects directly from DataFrames
#     # Create TSDataset objects from NumPy arrays
#     train_ds = TSDataset(train_df.to_numpy())  # Convert to NumPy array
#     valid_ds = TSDataset(valid_df.to_numpy())  # Convert to NumPy array
#     print('yes')
#     print(train_df.to_numpy().shape)
#     print(valid_df.to_numpy().shape)
#     # Define the model
#     model = RNN(
#         c_in=len(features),
#         c_out=1,
#         hidden_size=100,
#         n_layers=2,
#         bidirectional=True,
#         rnn_dropout=0.5,
#         fc_dropout=0.5
#     )

#     # Create TSDataLoaders
#     bs = 16
#     dls = TSDataLoaders.from_dsets(train_ds, valid_ds, bs=bs, num_workers=0, shuffle=False)

#     # Select MSE loss function
#     loss_func = nn.MSELoss()

#     # Create the Learner
#     learn = Learner(dls, model, loss_func=loss_func, metrics=accuracy)

#     # Train the model
#     learn.fit_one_cycle(1, 3e-3)  # Adjust epochs and learning rate
