import yfinance as yf

stock = input("Enter Your Stock: ")

stock = stock.upper()      # Convert into capital letters

share = yf.Ticker(stock)

price = share.history(period="1d")    # Get today's stock data

current_price = price["Close"]

current_price = current_price.iloc[-1]    # Last closing price

print("The value of " + stock + " is " + str(round(current_price, 2)))

#sir jo bataye the udemy wale wo code nahi hai ye, ye dusara code hai keuki 2026 me aisa hi code chalta hai aur sir ka 2015 ka code tha wo
