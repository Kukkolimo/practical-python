# mortgage.py
#
# Exercise 1.7
principal = 500000
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_months = 12
extra_money = 1000
months = 0

extra_payment_start_month = 61
extra_payment_end_month = 121
extra_payment = 1000

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment  
    months = months + 1
    print('{};{}'.format(months, total_paid))


print('Total paid', total_paid)
print('Months paid', months)