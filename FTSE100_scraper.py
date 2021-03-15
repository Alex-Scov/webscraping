# import relevant libraries

import requests
import pymysql
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date


# create empty lists for data to be appended into.

stock_code = []
company_name = []
stock_price = []
percent_change = []

# Base url of pages to be scraped.

url = "https://www.londonstockexchange.com/indices/ftse-100/constituents/table"

def url_iterator():
    for i in range(1, 7):# 6 pages of data to be scraped.
        newurl = url + "?page=" + str(i)
        page = requests.get(newurl)
        page_soup = BeautifulSoup(page.text, "html.parser")
        rows = page_soup.find_all('tr', attrs={'class':'medium-font-weight slide-panel'})
        for i in rows:# Get stock code.
            row = i.find_all('td')
            stock = row[0].text
            stock_code.append(stock)
        for i in rows:# Get company name and strip excess data.
            row = i.find_all('td')
            full_name = row[1].text.split()
            full_name.pop(-1)
            full_name.pop(-1)
            stripped_name = ' '.join(full_name)
            company_name.append(stripped_name)
        for i in rows:# Get stock price.
            row = i.find_all('td')
            price = row[4].text
            stock_price.append(price)
        for i in rows:# Get price change.
            row = i.find_all('td')
            change = row[6].text
            percent_change.append(change)

# Call function.

url_iterator()

# Create 2d array using numpy by casting list of lists to array.

list_of_lists = [stock_code, company_name, stock_price, percent_change]
stock_array = np.array(list_of_lists)

# Transpose array (invert horizontal and vertical axis) to get correct number of columns and rows.

t_array = np.transpose(stock_array)
df = pd.DataFrame(t_array, columns=['Stock Code', 'Company Name', 'Stock Price', 'Price Change (%)'])
print(df)

# def main():
#     connection = pymysql.connect(host = 'localhost', port = 33066, user = 'root', password = 'password', database = 'FTSE-100')

#     cursor = connection.cursor()
#     for ticker in stock_code:
#         cursor.execute(f'INSERT INTO security (ticker) VALUES ({ticker})')
#     for company in company_name:
#         cursor.execute(f'INSERT INTO security (company_name) VALUES ({company})')
#     for price in stock_price:
#         cursor.execute(f'INSERT INTO daily_price (stock_price) VALUES {price}')
#     for percent in percent_change:
#         cursor.execute(f'INSERT INTO daily_price (percent_change) VALUES {percent}')
#     cursor.close()
#     connection.close()

# main()

# if __name__ == '__main__':
#     main()

# def printname():
#     print(__name__)

# def insert_name():
#     cursor.execute('INSERT INTO' customers (fname_column, sname_column) VALUES (fname, sname))

#     , Company-name, Stock-price, Price-change