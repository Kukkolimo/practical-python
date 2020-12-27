# pcost.py
#
# Exercise 1.27 /1.30 function / 1.32 csv module
       
def portfolio_cost(filename):
    'This function will calculate total cost given the input file'
    total_price = 0
    with open(filename, 'rt') as f:
        headers = next(f).split(',')    
        for line in f:
            row = line.split(',')
            try:
                total_price = total_price + int(row[1]) * float(row[2])
            except ValueError:
                print("Could't parse", line)
        return(total_price)        

cost = portfolio_cost('data/portfolio.csv')
print('Total cost: ', cost)



    