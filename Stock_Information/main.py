import six
import yfinance as yf

stockSymbol = input("Enter your stock: ")

if stockSymbol.isalpha():
    print("boobies")
else:
    print("Please enter an actual ticker.")


tickerData = yf.Ticker(stockSymbol)

tickerDf = tickerData.history(period='1d')

print(tickerDf)


