'''
b = "Hello, World!"
print(b[2:5])
print(b[0:])


# create format string in python
a = "Hello, %s" % "World"
print(a)

c ='krishna'
c ="krishnaS"
c= 3.5666
print(c)


remainder = 7 // 3
print(remainder)


first = 'Test '
second = 5

print(first * second)



inp = input()
print(inp)



productId = 1222
print(productId)


words = ['one', 'two', 'three']

for word in words:
    print(word)

    

    bad name = 5


months = 'march'
print(month)



principal = 327.68
interest = principal * rate

print(interest)

x =-5
if x > 0 :
    print('x is positive')
else if:
    print('x is negative')


if x < 0 :
    pass # need to handle negative values!



tempValue =int('32')
print(tempValue)

print(float('32'))


import math

ratio = 10 / 5
decibels = 10 * math.log10(ratio)
print(decibels)


import random

for i in range(10):
    x = random.random()
    print(x)



def addtwonumbers(a, b):
    return a + b

print(addtwonumbers(5, 6))
print('add')




def print_twice(bruce):
    print(bruce)
    print(bruce)


import math
radians = 333
x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2
print(golden)


def print_twice(bruce):
    print(bruce)
    print(bruce)

result = print_twice('Bing')
print(result)


n = 10
while True:
    print(n, end=' ')
    n = n - 1    
print('Done!')


while True:
    line = input()
    if line == 'done':
        break
    print(line)
    print('Done!')



count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1

print('Count: ', count)


total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar

print('Total: ', total)


largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
        print('Loop:', itervar, largest)
print('Largest:', largest)


smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)




fruit = 'banana'
letter = fruit[1]

print(letter)


fruit = 'banana'
length = len(fruit)
last = fruit[length-1]
print(last)


fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1


fruit = 'banana'
fruit[3:3]



greeting = 'Hello, world!'
greeting[0] = 'J'
print(greeting)


greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)



word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


if word == 'banana':
 print('All right, bananas.')

'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))