def evaluate(hourly, daily):
    alerts = []

    if max(hourly["temperature_2m"]) > 40:
        alerts.append("🔥 Heatwave Alert")

    if max(hourly["precipitation_probability"]) > 60:
        alerts.append("☔ Rain Alert")

    if max(hourly["wind_speed_10m"]) > 15:
        alerts.append("🌪️ Wind Alert")

    return alerts