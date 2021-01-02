# report.py
#
# Exercise 2.4 / 2.5 / 2.6
import csv
def read_portfolio(filename):
    'This function will open a given portfolio file and convert it to list of tuples'
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            holding = {'name'  :row[0], 
                       'shares':int(row[1]), 
                       'price' :float(row[2])}
            #holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    'This function will create a dictionary of stock prices per given file'
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)        
        for row in rows:
            if len(row) == 0:
                continue
            else:
                prices[row[0]] = float(row[1])       
    return prices

def print_file(filename):
    'This function will print the contents of a csv file'
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:           
            print(row, len(row))

def gain_loss(portfolio, prices):
    for stock in portfolio:
        stock['purchased_value'] = round(stock['price'] * stock['shares'],2)
        stock['current_value'] = stock['shares'] * prices.get(stock['name'])
        stock['gain/loss'] = stock['current_value'] - stock['purchased_value']
        #print(stock['name'], prices.get(stock['name']))
    return portfolio
        



            