from __future__ import annotations

import os
import requests


def get_air_pollution(api_key: str, lat: float, lon: float) -> dict:
    url = "https://api.openweathermap.org/data/2.5/air_pollution"
    params = {"lat": lat, "lon": lon, "appid": api_key}
    r = requests.get(url, params=params, timeout=15)
    r.raise_for_status()
    return r.json()


def format_air_quality(aqi: int) -> str:
    # OpenWeather AQI scale: 1..5
    mapping = {
        1: "Good",
        2: "Fair",
        3: "Moderate",
        4: "Poor",
        5: "Very Poor",
    }
    return mapping.get(aqi, "Unknown")


def main() -> None:
    api_key = os.getenv("OPENWEATHER_API_KEY") or input("Enter your OpenWeather API key: ").strip()
    if not api_key:
        print("Error: API key is required.")
        return

    try:
        lat = float(input("Enter latitude: ").strip())
        lon = float(input("Enter longitude: ").strip())
    except ValueError:
        print("Error: latitude/longitude must be numbers.")
        return

    try:
        data = get_air_pollution(api_key, lat, lon)
        items = data.get("list", [])
        if not items:
            print("No air pollution data returned.")
            return

        first = items[0]
        aqi = first.get("main", {}).get("aqi")
        comps = first.get("components", {})

        print("\n==============================")
        print("Air Pollution")
        print("==============================")
        if aqi is not None:
            print(f"AQI: {aqi} ({format_air_quality(aqi)})")

        # Common pollutants (µg/m3)
        for k in ["co", "no", "no2", "o3", "so2", "pm2_5", "pm10", "nh3"]:
            if k in comps:
                print(f"{k.upper():5}: {comps[k]}")
        print("==============================\n")

    except Exception as e:
        print(f"Could not retrieve air pollution data: {e}")


if __name__ == "__main__":
    main()
