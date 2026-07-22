#Ye sir ka code hai 2015 ke according jo abhi work nahi karta hai
import re
import urllib.request

try:
    url = "http://dictionary.reference.com/browse/"
    word = input("Enter your word: ")
    url = url + word
    data = urllib.request.urlopen(url).read()
    data1 = data.decode("utf-8")
    m = re.search('meta name="description" content="', data1)
    start = m.end()
    end = start + 300
    newString = data1[start: end]
    m = re.search("See more.", newString)
    end = m.start() - 1
    definition = newString[0:end]
    print(definition)
except:
    print("I'm sorry, you're word is not in the dictionary.")

#Aur ye mera code hai jo maine chatgpt ke help se nikala hai ye code khoj ke
import requests

city = input("Enter your city: ")

url = f"https://wttr.in/{city}?format=3"

weather = requests.get(url)

print(weather.text)
