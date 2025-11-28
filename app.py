import streamlit as st
import streamlit as st
import requests
import pandas as pd



'''
# TaxiFareModel front
'''

url = 'https://taxifare.lewagon.ai/predict'

pickup_datetime = st.text_input("Pickup datetime", "2014-07-06 19:18:00")
pickup_longitude = st.number_input("Pickup longitude", value=-73.950655)
pickup_latitude = st.number_input("Pickup latitude", value=40.783282)
dropoff_longitude = st.number_input("Dropoff longitude", value=-73.984365)
dropoff_latitude = st.number_input("Dropoff latitude", value=40.769802)
passenger_count = st.number_input("Passenger count", value=1)

params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

response = requests.get(url, params=params)
result = response.json()
fare = result['fare']

map_df = pd.DataFrame(
    [
        {"lat": pickup_latitude, "lon": pickup_longitude},   # pickup
        {"lat": dropoff_latitude, "lon": dropoff_longitude}  # dropoff
    ]
)

st.map(map_df)

st.markdown(f"💵 Predicted fare: **${fare:.2f}**")
