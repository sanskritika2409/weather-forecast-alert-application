import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Weather Alert Dashboard", layout="wide")

st.title("🌦️ Weather Forecast & Alert Dashboard")

city = st.text_input("Enter City", "Delhi")

if st.button("Get Weather"):

    lat, lon = 28.61, 77.20  # default Delhi (can improve later with geocoding)

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,precipitation_probability,wind_speed_10m&daily=temperature_2m_max,temperature_2m_min&current_weather=true"

    response = requests.get(url).json()

    st.subheader("📍 Current Weather")
    st.json(response["current_weather"])

    st.subheader("📊 Hourly Data")

    df = pd.DataFrame(response["hourly"])
    st.dataframe(df.head(20))

    st.subheader("📈 Temperature Trend")
    st.line_chart(df["temperature_2m"])

    st.subheader("⚠️ Simple Alerts")

    alerts = []

    if max(df["temperature_2m"]) > 40:
        alerts.append("🔥 Heatwave Alert")

    if max(df["precipitation_probability"]) > 60:
        alerts.append("☔ Rain Alert")

    if max(df["wind_speed_10m"]) > 15:
        alerts.append("🌪️ Wind Alert")

    for a in alerts:
        st.error(a)

    if not alerts:
        st.success("No Alerts — Weather is Normal 😊")