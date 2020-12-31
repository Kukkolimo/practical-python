# report.py
#
# Exercise 2.4
import csv
def read_portfolio(filename):
    'This function will open a given portfolio file and convert it to list of tuples'
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio
