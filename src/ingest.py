import httpx

def fetch_open_meteo(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,precipitation_probability,wind_speed_10m&daily=temperature_2m_max,temperature_2m_min&current_weather=true"

    r = httpx.get(url)
    return r.json()