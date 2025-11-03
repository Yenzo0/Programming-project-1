#Assignment: Programming Project #1
#Name:Hugo Pires Almeida

class WeatherDay:
    def __init__(self, rain, wind):
        self.rain = rain
        self.wind = wind

class WeatherStats:
    def __init__(self):
        self.days = []

    def add_day(self, rain, wind):
        self.days.append(WeatherDay(rain, wind))

    def average_rain(self):
        return sum(d.rain for d in self.days) / len(self.days)

    def average_wind(self):
        return sum(d.wind for d in self.days) / len(self.days)

    def severity(self):
        return (self.average_rain() * 10) + self.average_wind()

weather = WeatherStats()

print("Enter rain and wind for each day (end with -1.0):")

while True:
    data = input().strip()
    if not data:
        continue
    values = data.split()
    rain = float(values[0])
    if rain == -1.0:
        break
    wind = float(values[1])
    weather.add_day(rain, wind)

if weather.days:
    print(f"\nDays recorded: {len(weather.days)}")
    print(f"Average rain: {weather.average_rain():.2f}")
    print(f"Average wind: {weather.average_wind():.2f}")
    print(f"Weather severity: {weather.severity():.2f}")
else:
    print("No weather data entered.")

