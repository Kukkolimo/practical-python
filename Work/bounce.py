# bounce.py
#
# Exercise 1.5
h = 100
b = 3/5
n = 10

while n > 0:
    h = round(h*b, 4)
    n = n - 1
    print(h)
