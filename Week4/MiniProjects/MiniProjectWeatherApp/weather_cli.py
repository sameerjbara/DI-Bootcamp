from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import os
import pytz

from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError


@dataclass
class CityInfo:
    city_id: int
    name: str
    country: str
    lat: float
    lon: float


def format_local_time(ts_utc: int, tz_name: str) -> str:
    tz = pytz.timezone(tz_name)
    dt = datetime.fromtimestamp(ts_utc, tz=pytz.utc).astimezone(tz)
    return dt.strftime("%Y-%m-%d %H:%M:%S %Z")


def get_city_info_by_name(owm: OWM, city_query: str) -> CityInfo:
    """
    Use PyOWM city ID registry to get the city ID (and coords) from a city name.
    If multiple matches exist, uses the first match.
    """
    city_query = city_query.strip()
    if not city_query:
        raise ValueError("City name cannot be empty.")

    registry = owm.city_id_registry()
    ids = registry.ids_for(city_query)
    if not ids:
        raise NotFoundError(f"City not found: {city_query}")

    city_id = ids[0]
    loc = registry.location_for(city_id)

    return CityInfo(
        city_id=city_id,
        name=loc.name,
        country=loc.country,
        lat=float(loc.lat),
        lon=float(loc.lon),
    )


def display_current_weather(owm: OWM, city: CityInfo, tz_name: str) -> None:
    mgr = owm.weather_manager()
    obs = mgr.weather_at_id(city.city_id)
    w = obs.weather

    temp = w.temperature("celsius")
    wind = w.wind()  # dict like {'speed': x, 'deg': y, 'gust': z}
    humidity = w.humidity
    clouds = w.clouds

    sunrise_utc = w.sunrise_time(timeformat="unix")
    sunset_utc = w.sunset_time(timeformat="unix")

    print("\n==============================")
    print(f"Weather for: {city.name}, {city.country} (city_id={city.city_id})")
    print("==============================")
    print(f"Status: {w.status} ({w.detailed_status})")
    print(f"Temperature: {temp.get('temp')}°C (feels like {temp.get('feels_like')}°C)")
    print(f"Min/Max: {temp.get('temp_min')}°C / {temp.get('temp_max')}°C")
    print(f"Humidity: {humidity}% | Clouds: {clouds}%")

    # Wind info
    speed = wind.get("speed")
    deg = wind.get("deg")
    gust = wind.get("gust")
    wind_line = f"Wind: {speed} m/s"
    if deg is not None:
        wind_line += f" | Direction: {deg}°"
    if gust is not None:
        wind_line += f" | Gust: {gust} m/s"
    print(wind_line)

    # Sunrise / Sunset
    print(f"Sunrise: {format_local_time(sunrise_utc, tz_name)}")
    print(f"Sunset : {format_local_time(sunset_utc, tz_name)}")
    print("==============================\n")


def main() -> None:
    api_key = os.getenv("OPENWEATHER_API_KEY") or input("Enter your OpenWeather API key: ").strip()
    if not api_key:
        print("Error: API key is required.")
        return

    owm = OWM(api_key)

    # 1) Paris (required)
    try:
        paris = get_city_info_by_name(owm, "Paris")
        display_current_weather(owm, paris, tz_name="Europe/Paris")
    except Exception as e:
        print(f"Could not retrieve Paris weather: {e}")

    # 2) User location (required)
    user_city = input("Enter a location (city name, e.g., 'Tel Aviv'): ").strip()
    if not user_city:
        print("No location entered. Exiting.")
        return

    tz_name = input("Enter timezone name (e.g., 'Asia/Jerusalem') or press Enter for UTC: ").strip() or "UTC"

    try:
        city = get_city_info_by_name(owm, user_city)
        display_current_weather(owm, city, tz_name=tz_name)

        # Print coords so the next file (air pollution) can use them
        print(f"Coordinates for Air Pollution API: lat={city.lat}, lon={city.lon}")
    except Exception as e:
        print(f"Could not retrieve weather for '{user_city}': {e}")


if __name__ == "__main__":
    main()
