import sys
import yfinance as yf

stockSymbol = input("Enter your stock: ")

tickerData = yf.Ticker(stockSymbol)

tickerDf = tickerData.history(period='1d', start='2020-1-1', end='2020-1-24')

print(tickerDf)


