import requests
from bs4 import BeautifulSoup
data = requests.get('http://www.synonym.com/antonyms/cold/')
soup = BeautifulSoup(data.text, 'html.parser')
data2 = soup.find('span', {})
data2 = soup.find('span', {'class':'equals'})
print(data2)
print(data2.string)
print(data2.contents)

#its not working, because the code is according to the 2015year, its not working in today's
