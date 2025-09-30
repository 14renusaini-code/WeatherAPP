import src.weather as weather
import src.utils as utils

def main():
    city = input("Enter city name: ")
    data = weather.fetch_weather(city)
    print(utils.format_weather(data))

if __name__ == "__main__":
    main()
