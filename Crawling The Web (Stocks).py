import re
import urllib.request
#https://www.google.com/finance?q=
url = "https://www.google.com/finance?q="
stock = input("Enter Your Stock: ")
url = url + stock #Concatenation of string
print(url)
data = urllib.request.urlopen(url).read()
data1 = 
