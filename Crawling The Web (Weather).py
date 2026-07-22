import requests

city = input("Enter your city: ")

url = f"https://wttr.in/{city}?format=3"

weather = requests.get(url)

print(weather.text)
