from decimal import Decimal
import math

import random

f = 3.14
d = Decimal("3.14")

print(type(f), f)  # <class 'float'> 3.14
print(type(d), d)  # <class 'decimal.Decimal'> 3.14

print("""Hello, World!
    programming is fun.
    sdfsdfs
    computer science is the best.

""")

names ='John kumar'
#print(names.count('h'))  # 1

x=6
y=5
if x > y: 
    print(x)
print(y)  # 6 

x=9
if x % 2 == 0:
 print('x is even')
else:
 print('x is odd')


if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')


if 0 < x:
    if x < 10:
     print('x is a positive single-digit number.')


inp = input('Enter Fahrenheit Temperature: ')
fahr = float(inp)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)


inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')

x = 6 
y = 0
    
# 5

i=3

for i in range(100):
 x = random.randint(5, 10)
 print(x)

for i in 20:
  print(i)
 