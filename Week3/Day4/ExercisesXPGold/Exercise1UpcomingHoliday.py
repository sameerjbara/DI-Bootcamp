# Instructions
# Write a function that displays today’s date.
# The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is New Years’ Eve in 30 days).
# Hint: Use a module to find the datetime and name of the upcoming holiday.


import datetime
import holidays


def next_holiday(country_code="US", years_ahead=2):
    today = datetime.date.today()
    print("Today's date:", today)

    years = [today.year + i for i in range(years_ahead + 1)]
    cal = holidays.country_holidays(country_code, years=years)

    upcoming = []
    for day, name in cal.items():
        if day >= today:
            upcoming.append((day, name))

    if not upcoming:
        print("No upcoming holidays found.")
        return

    upcoming.sort(key=lambda x: x[0])
    day, name = upcoming[0]

    delta = day - today
    print(f"Next holiday: {name} on {day} (in {delta.days} days)")


# Example:
if __name__ == "__main__":
    next_holiday("US")   # change to your country code, e.g. "IL"
