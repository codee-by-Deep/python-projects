import requests


def weather_app():
    api_key = "somekey123"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    print(data)
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}'C")
    print(f"Feels like: {data['main']['feels_like']}'C")
    print(f"Humidity: {data['main']['humidity']} %")
    print(f"Country: {data['sys']['country']}")
    print(f"Condition: {data['weather'][0]['description']}")
    
while True:
    weather_app()
    again = input("Want to check for another city (y/n): ")
    if again == "n":
        break    
