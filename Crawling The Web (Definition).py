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

#sir jo bataye the udemy wale wo code nahi hai ye, ye dusara code hai keuki 2026 me aisa hi code chalta hai aur sir ka 2015 ka code tha wo
