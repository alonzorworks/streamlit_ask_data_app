import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
import plotly.graph_objects as go

def forecast_high_low_lstm(df):
    """
    Predicts high and low values using LSTM and creates a candle chart with forecast markers.

    Args:
        df (pd.DataFrame): DataFrame containing time series data with "Date", "Open", "High", "Low", "Close" columns.

    Returns:
        None
    """
    print("df= ", df.shape)
    # Scale high and low values
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(df[["High", "Low"]].values)
    print(scaled_data)

    # Create training and testing sets
    train_size = int(len(scaled_data) * 0.8)
    train, test = scaled_data[0:train_size, :], scaled_data[train_size:len(scaled_data), :]

    print("train= ",train.shape)
    print("test= ", test.shape)

    # Create input sequences for LSTM
    def create_dataset(dataset, look_back=1):
        X, Y = [], []
        for i in range(len(dataset) - look_back - 1):
            a = dataset[i:(i + look_back), :]
            X.append(a)
            Y.append(dataset[i + look_back, :])
        return np.array(X), np.array(Y)

    look_back = 1
    X_train, Y_train = create_dataset(train, look_back)
    X_test, Y_test = create_dataset(test, look_back)
    print("X_train", X_train.shape)
    print("X_test", X_test.shape)

    # Reshape input for LSTM
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], X_train.shape[2]))
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], X_test.shape[2]))

    print("X_train= ", X_train.shape)
    print("X_test= ", X_test.shape)

    # Build LSTM model
    model = Sequential()
    model.add(LSTM(100, input_shape=(look_back, 2), return_sequences=True))
    model.add(Dropout(0.2))  # Add dropout for regularization
    model.add(LSTM(100))
    model.add(Dropout(0.2))
    model.add(Dense(2))
    model.compile(loss='mean_squared_error', optimizer='adam')

    # Train LSTM model
    model.fit(X_train, Y_train, epochs=200, batch_size=64, verbose=2)

    # Make predictions for future periods
    high_forecast = []
    low_forecast = []
    for i in range(5):
        X_forecast = np.array([scaled_data[-look_back:]])
        X_forecast = np.reshape(X_forecast, (X_forecast.shape[0], X_forecast.shape[1], X_forecast.shape[2]))
        pred = model.predict(X_forecast)[0]
        high_forecast.append(pred[0])
        low_forecast.append(pred[1])
        scaled_data = np.append(scaled_data, [pred], axis=0)

    # Convert high_forecast and low_forecast to NumPy arrays
    high_forecast = np.array(high_forecast).reshape(-1, 1)
    low_forecast = np.array(low_forecast).reshape(-1, 1)
    
    # Adjust shapes before inverse transform
    high_forecast = np.hstack([high_forecast, np.zeros_like(high_forecast)])
    low_forecast = np.hstack([low_forecast, np.zeros_like(low_forecast)])


    print('Yes')
    print(high_forecast.shape)
    print(low_forecast.shape)
    # Inverse transform forecasts back to original scale (corrected reshaping)
    high_forecast = scaler.inverse_transform(high_forecast)  
    low_forecast = scaler.inverse_transform(low_forecast)

    # Print shapes after inverse transform
    print("High Forecast After", high_forecast.shape)
    print("Low Forecast After", low_forecast.shape)

    # Find range of low and high values (including forecasts)
    low_range = min(df["Low"].min(), np.min(low_forecast))
    high_range = max(df["High"].max(), np.max(high_forecast))

    # Create candle chart
    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        increasing_line_color="green",
        decreasing_line_color="red"
    )])

    # Add forecast as markers (for both High and Low)
    fig.add_trace(go.Scatter(
        x=df.index[-5:],
        y=high_forecast,
        mode="markers",
        marker=dict(size=15, color="blue", symbol="triangle-up"),
        name="High Forecast"
    ))
    fig.add_trace(go.Scatter(
        x=df.index[-5:],
        y=low_forecast,
        mode="markers",
        marker=dict(size=15, color="red", symbol="triangle-down"),
        name="Low Forecast"
    ))

    # Customize the chart
    fig.update_layout(
        title="Candle Chart with High/Low LSTM Forecast",
        yaxis_range=[low_range - 0.1 * (high_range - low_range), high_range + 0.1 * (high_range - low_range)]
    )

    # Display the chart
    return fig


