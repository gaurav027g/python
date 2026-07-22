import requests

city = input("Enter your city: ")

url = f"https://wttr.in/{city}?format=3"

weather = requests.get(url)

print(weather.text)

#sir jo bataye the udemy wale wo code nahi hai ye, ye dusara code hai keuki 2026 me aisa hi code chalta hai aur sir ka 2015 ka code tha wo
