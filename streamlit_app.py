import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load your S&P 500 data from a CSV file (Adjust the path to your file)
@st.cache
def load_data():
    data = pd.read_csv("data/USA500IDXUSD_D1.csv")
    return data
    print(data.head())

data = load_data()

# Checkboxes to filter data based on high-impact news
st.sidebar.subheader("Filter Data")
high_impact_news = st.sidebar.checkbox("Include Only High Impact News Days", value=False)

# Filter data based on high-impact news
if high_impact_news:
    data = data[data['High_Impact_News'] == True]

# Calculate average yield for each day of the week
day_of_week_avg_yield = data.groupby('DayOfWeek')['Yield'].mean()

# Calculate average yield for each week of the year
week_of_year_avg_yield = data.groupby('WeekOfYear')['Yield'].mean()

# Calculate average yield for each month of the year
month_avg_yield = data.groupby('Month')['Yield'].mean()

# Display average yield by day of the week
st.subheader("Average Yield by Day of the Week")
st.bar_chart(day_of_week_avg_yield)

# Display average yield by week of the year
st.subheader("Average Yield by Week of the Year")
st.bar_chart(week_of_year_avg_yield)

# Display average yield by month of the year
st.subheader("Average Yield by Month of the Year")
st.bar_chart(month_avg_yield)

# Minimum and Maximum Yield
min_yield = data['Yield'].min()
max_yield = data['Yield'].max()

st.subheader("Historical Minimum and Maximum Yield")
st.write(f"Minimum Yield: {min_yield}")
st.write(f"Maximum Yield: {max_yield}")

# Display the DataFrame
st.subheader("S&P 500 Data")
st.write(data)
