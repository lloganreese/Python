import yfinance as yf
import sys

def main():
    menu()

def tickerInfo():
    stockSymbol = input("Enter your stock: ")
    tickerData = yf.Ticker(stockSymbol)
    tickerDf = tickerData.history(period='1d')
    print(tickerDf)

def menu():
    print("****************STOCK INFORMATION****************")
    print()

    userSelection = int(input(""" 
                                1: Find Ticker Info
                                2: Exit 
                                
                                Make a selection: """))
    if userSelection == 1:
        tickerInfo()
    elif userSelection == 2:
        exit()
    else:
        print("You must choose from the options provided")
        menu()


main()