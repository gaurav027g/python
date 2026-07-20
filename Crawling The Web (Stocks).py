import re
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#https://www.google.com/finance?q=
url = "https://www.google.com/finance?q="
stock = input("Enter Your Stock: ")
url = url + stock #Concatenation of string
print(url)
data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
print(data1)

p = re.search('meta itemprop="price"',data1)
print(p)
