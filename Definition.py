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

word = input("Enter a word: ")

url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\nWord :", data[0]["word"])
    print("Meaning :", data[0]["meanings"][0]["definitions"][0]["definition"])

else:
    print("Word not found.")

