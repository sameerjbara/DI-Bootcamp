# Instructions
# Given an age in seconds, calculate how old someone would be on all those planets :

# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Example : if someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years



def age_on_planets(seconds):
    earth_year_seconds = 31557600  # 365.25 days
    earth_years = seconds / earth_year_seconds

    orbital_periods = {
        "Earth": 1.0,
        "Mercury": 0.2408467,
        "Venus": 0.61519726,
        "Mars": 1.8808158,
        "Jupiter": 11.862615,
        "Saturn": 29.447498,
        "Uranus": 84.016846,
        "Neptune": 164.79132,
    }

    results = {}
    for planet, period in orbital_periods.items():
        results[planet] = round(earth_years / period, 2)

    return results


# Example:
print(age_on_planets(1_000_000_000))
# Earth should be about 31.69
