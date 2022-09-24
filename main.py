# INF601 - Advanced Programming in Python
# Michael Flavin
# Mini Project 1


import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt




def stock_func(ticker):

    data = yf.download(ticker, start="2022-08-30", end="2022-09-14")

    msftPrices = []

    for price in data['Adj Close']:
        msftPrices.append(price)

    print(msftPrices)

    ticker_array = np.array(msftPrices)

    plt.plot(ticker_array)

    plt.savefig('charts/' + ticker + '.png')

    plt.show()



ticker_1 = "AAPL"

ticker_2 = "MSFT"

ticker_3 = "TSLA"

ticker_4 = "AFL"

ticker_5 = "NVDA"



stock_func(ticker_1)

stock_func(ticker_2)

stock_func(ticker_3)

stock_func(ticker_4)

stock_func(ticker_5)