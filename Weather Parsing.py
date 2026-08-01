import requests
from bs4 import BeautifulSoup

url = "https://www.accuweather.com/en/in/khirhar/192409/weather-forecast/192409"
data = requests.get(url)
soup = BeautifulSoup(data.text, "html.parser")
print(data)
print(soup.find('div'))
print(soup.find('div', {'class':'info'}))
data2 = soup.find('div', {'class':'info'})
data3 = data2.find('strong', {'class':'temp'})
print(data3)
print(data3.contents)
print(data3.contents[0])