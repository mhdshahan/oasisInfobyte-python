print("Basic Weather App")
import requests
#Defining a function
def get_weather(city):
    api_key = '642c8a0571e3faeec1d7279007a90790'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'
    url = f'{base_url}q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        weather = {
            'description': data['weather'][0]['description'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return {'error': 'City not found'}
#Define main function
def main():
    city = input("Enter city name: ")
    weather = get_weather(city)
    if 'error' in weather:
        print(weather['error'])
    else:
        print(f"Weather in {city}:")
        print(f"Description: {weather['description']}")
        print(f"Temperature: {weather['temperature']} Kelvin")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} meter/sec")
#Calling the main function
if __name__ == "__main__":
    main()
