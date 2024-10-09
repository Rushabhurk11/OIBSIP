import requests
import sys

# Function to get weather data for a given city using OpenWeatherMap API
def get_weather(city, api_key):
    # OpenWeatherMap URL with units set to metric (Celsius)
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
    # base_url = http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API key}

    # Send a request to the OpenWeatherMap API
    response = requests.get(base_url)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        data = response.json()
        
        # Parse the required weather details
        city_name = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_desc = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        country = data['sys']['country']

        # Print the weather details
        print(f"Weather in {city_name}, {country}:")
        print(f"  Temperature   : {temperature}°C")
        print(f"  Humidity      : {humidity}%")
        print(f"  Weather       : {weather_desc.capitalize()}")
        print(f"  Wind Speed    : {wind_speed} m/s")
    else:
        print("City not found or invalid API key. Please check your inputs.")

# Entry point of the program
def main():
    # API key for OpenWeatherMap (replace with your own API key)
    API_KEY = "add01eaec1ae3558f8f166396bf867b5"

    if len(sys.argv) < 2:
        print("Usage: python weather_app.py <city>")
        return

    # Get the city name from command-line arguments
    city = sys.argv[1]

    # Get the weather data for the given city
    get_weather(city, API_KEY)

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
