#Ye sir ka code hai 2015 ke according jo abhi work nahi karta hai
import re
import urllib.request
arrayofStocks = ["FB", "GOOG", "DATA", "BABA"]
url = "https://www.google.com/finance?q="
stock = input("Enter your stock: ")
url = url + stock
data= urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
m = re.search('meta itemprop="price"', data1)
start = m.start()
end = start + 50
newString = data1[start:end]
m = re.search('content="', newString)
start = m.end()
newString1 = newString[start:]
m = re.search("/", newString1)
start = 0
end = m.end()-3
final = newString1[0:end]
print("The value of " + stock.upper() + " is " + final)

#Aur ye mera code hai jo maine chatgpt ke help se nikala hai ye code khoj ke
import yfinance as yf

stock = input("Enter Your Stock: ")

stock = stock.upper()      # Convert into capital letters

share = yf.Ticker(stock)

price = share.history(period="1d")    # Get today's stock data

current_price = price["Close"]

current_price = current_price.iloc[-1]    # Last closing price

print("The value of " + stock + " is " + str(round(current_price, 2)))


