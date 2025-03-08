#!/usr/bin/env python
# coding: utf-8

# ## 1. Scrape Stock Data for a Single Company

# In[2]:


import yfinance as yf
import pandas as pd

# Define the ticker symbol for Tesla
ticker_symbol = 'TSLA'

# Fetch the stock data
stock = yf.Ticker(ticker_symbol)

# Extract the required information with checks for None values
stock_info = {
    'Stock Name': stock.info.get('longName', 'N/A'),
    'Price': stock.info.get('currentPrice', 'N/A'),
    'Change': stock.info.get('regularMarketChange', 'N/A'),
    'Previous Close': stock.info.get('previousClose', 'N/A'),
    'Open': stock.info.get('open', 'N/A'),
    'Bid': stock.info.get('bid', 'N/A'),
    'Ask': stock.info.get('ask', 'N/A'),
    "Day's Range": (
        f"{stock.info.get('dayLow', 'N/A')} - {stock.info.get('dayHigh', 'N/A')}"
        if stock.info.get('dayLow') is not None and stock.info.get('dayHigh') is not None
        else 'N/A'
    ),
    '52 Week Range': (
        f"{stock.info.get('fiftyTwoWeekLow', 'N/A')} - {stock.info.get('fiftyTwoWeekHigh', 'N/A')}"
        if stock.info.get('fiftyTwoWeekLow') is not None and stock.info.get('fiftyTwoWeekHigh') is not None
        else 'N/A'
    ),
    'Volume': stock.info.get('volume', 'N/A'),
    'Avg. Volume': stock.info.get('averageVolume', 'N/A'),
    'Market Cap': stock.info.get('marketCap', 'N/A'),
    'Beta': stock.info.get('beta', 'N/A'),
    'PE Ratio (TTM)': stock.info.get('trailingPE', 'N/A'),
    'EPS': stock.info.get('trailingEps', 'N/A'),
    'Earnings Date': (
        pd.to_datetime(stock.info.get('earningsDate', 'N/A')[0]).strftime('%Y-%m-%d')
        if stock.info.get('earningsDate') is not None
        else 'N/A'
    ),
    'Forward Dividend & Yield': (
        f"{stock.info.get('dividendRate', 'N/A')} "
        f"({stock.info.get('dividendYield', 0) * 100:.2f}%)"
        if stock.info.get('dividendYield') is not None
        else 'N/A'
    ),
    'Ex-Dividend Date': (
        pd.to_datetime(stock.info.get('exDividendDate', 'N/A')).strftime('%Y-%m-%d')
        if stock.info.get('exDividendDate') is not None
        else 'N/A'
    ),
    '1y Target Est': stock.info.get('targetMeanPrice', 'N/A')
}

# Convert the dictionary to a DataFrame
stock_df = pd.DataFrame([stock_info])

# Transpose the DataFrame to switch rows and columns
stock_df_transposed = stock_df.transpose()

# Save the transposed data to JSON, CSV, and Excel files
stock_df_transposed.to_json('TSLA_stock_data.json', orient='columns')
stock_df_transposed.to_csv('TSLA_stock_data.csv', header=False)
stock_df_transposed.to_excel('TSLA_stock_data.xlsx', header=False)

print("Stock data for TSLA saved to JSON, CSV, and Excel files in vertical format.")


# ## 2: Transpose Stock Data in Horizontal Format

# In[3]:


import pandas as pd

# Load the previously saved stock data
df = pd.read_json('TSLA_stock_data.json', lines=True)

# Transpose the DataFrame
df_transposed = df.transpose()

# Save the transposed data to Excel
df_transposed.to_excel('TSLA_stock_data_horizontal.xlsx', header=False)

print("Transposed stock data for TSLA saved to Excel.")


# ## 3. Stock Data with different companies.

# In[4]:


import yfinance as yf
import pandas as pd

# List of ticker symbols for the companies
ticker_symbols = ['TSLA', 'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB']

# Initialize an empty list to hold the stock information
stocks_info = []

# Loop through each ticker symbol
for ticker_symbol in ticker_symbols:
    # Fetch the stock data
    stock = yf.Ticker(ticker_symbol)
    info = stock.info

    # Extract the required information with checks for None values
    stock_info = {
        'Ticker Symbol': ticker_symbol,
        'Stock Name': info.get('longName', 'N/A'),
        'Price': info.get('currentPrice', 'N/A'),
        'Change': info.get('regularMarketChange', 'N/A'),
        'Previous Close': info.get('previousClose', 'N/A'),
        'Open': info.get('open', 'N/A'),
        'Bid': info.get('bid', 'N/A'),
        'Ask': info.get('ask', 'N/A'),
        "Day's Range": f"{info.get('dayLow', 'N/A')} - {info.get('dayHigh', 'N/A')}",
        '52 Week Range': f"{info.get('fiftyTwoWeekLow', 'N/A')} - {info.get('fiftyTwoWeekHigh', 'N/A')}",
        'Volume': info.get('volume', 'N/A'),
        'Avg. Volume': info.get('averageVolume', 'N/A'),
        'Market Cap': info.get('marketCap', 'N/A'),
        'Beta': info.get('beta', 'N/A'),
        'PE Ratio (TTM)': info.get('trailingPE', 'N/A'),
        'EPS': info.get('trailingEps', 'N/A'),
        'Earnings Date': info.get('earningsDate', 'N/A'),
        'Forward Dividend & Yield': (
            f"{info.get('dividendRate', 'N/A')} ({info.get('dividendYield', 0) * 100:.2f}%)"
            if info.get('dividendYield') is not None else 'N/A'
        ),
        'Ex-Dividend Date': info.get('exDividendDate', 'N/A'),
        '1y Target Est': info.get('targetMeanPrice', 'N/A')
    }

    # Append the dictionary to the list
    stocks_info.append(stock_info)

# Convert the list of dictionaries to a DataFrame
stocks_df = pd.DataFrame(stocks_info)

# Save the data to an Excel file
stocks_df.to_excel('stocks_data.xlsx', index=False)

