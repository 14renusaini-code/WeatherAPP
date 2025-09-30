def format_weather(data):
    if not data:
        return "No data available."
    city = data.get('name')
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    return f"Weather in {city}:\nTemperature: {temp}°C\nDescription: {desc}"

# You can add more utility functions here
