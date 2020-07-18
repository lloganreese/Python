import sys
import yfinance as yf

def main():
    menu()

def menu():
    print("\n*********************************************")
    print("************** Options Pricing **************")
    print("*********************************************\n")

    #variables defined
    optionType = int(input("Is this a 1. Call or a 2. Put?: "))
    
    if optionType == 1:
        callOption()
    elif optionType == 2:
        putOption()
    else:
        print("\nPlease enter either 1 or 2 for selection.")
        menu()
        
    currentPrice = input("Please enter the current stock price: ")
    strikePrice = input("Please enter the chosen strike price: ")
    optionPrice = input("Please enter the price paid for the option: ")
    cashITM = input("How far in the money do you expect this option?: ")
    percentGain = input("How much are you expecting to gain(%)?: ")
    

def callOption():
    print("\nYou have selected call.\n")

def putOption():
    print("\nYou have selected put.\n")

main()

