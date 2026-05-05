from src.ingest import fetch_open_meteo
from src.rules import evaluate
import pandas as pd

def run(city="Delhi", lat=28.61, lon=77.20):
    print("\n🌦️ Weather Forecast System\n")

    data = fetch_open_meteo(lat, lon)

    current = data["current_weather"]
    print("📍 Current Weather:")
    print(current)

    hourly = data["hourly"]

    df = pd.DataFrame(hourly)

    alerts = evaluate(hourly, data["daily"])

    print("\n⚠️ ALERTS:")
    for a in alerts:
        print(a)

    df.to_csv("reports/weather_report.csv", index=False)
    print("\n✅ Report saved!")

if __name__ == "__main__":
    run()