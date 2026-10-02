# [10, 20, 30, 40]
# ['crunchy frog', 'ram bladder', 'lark vomit']

# ['spam', 2.0, 5, [10, 20]]


# cheeses = ['Cheddar', 'Edam', 'Gouda']
# numbers = [17, 123]
# empty = []
# print(cheeses, numbers, empty)
# print(cheeses[0])

#print(len(cheeses[0]))

# for chees in cheeses:
#     print(chees)

# for i in range(len(cheeses)):
#     print(i, cheeses[i])


# numbers = [17, 123]
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
# print(numbers)


# for x in empty:
#     print('This never happens.')

# number =['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
# print(len(number))

# a = [1, 2, 3]
# b = [4, 5, 6]
# c= a + b
# print(c)


# print([0] * 4)

# print([1, 2, 3] * 3) #three time  [1, 2, 3, 1, 2, 3, 1, 2, 3]


# list slices

# t = ['a', 'b', 'c', 'd', 'e', 'f']
# print(t[1:3])



# List methods
# t = ['a', 'b', 'c']
# t.append('d')
# print(t)


# t1 = ['a', 'b', 'c']
# t2 = ['d', 'e']
# t1.extend(t2)
# print(t1)


# t = ['d', 'c', 'e', 'b', 'a']
# t.sort()
# print(t)


 #Deleting elements

# t = ['a', 'b', 'c']
# x = t.pop(1)
# print(t)

# t = ['a', 'b', 'c']
# del t[1]
# print(t)

# t = ['a', 'b', 'c']
# t.remove('b')
# print(t)


# t = ['a', 'b', 'c', 'd', 'e', 'f']
# del t[1:5]
# print(t)

# Lists and functions
# nums = [3, 41, 12, 9, 74, 15]
# print(len(nums))
# print(max(nums))
# print(min(nums))
# print(sum(nums))


# total = 0
# count = 0
# while (True):
#     inp = input('Enter a number: ')
#     if inp == 'done': break
#     value = float(inp)
#     total = total + value
#     count = count + 1

# average = total / count
# print('Average:', average)



# numlist = list()
# while (True):
#     inp = input('Enter a number: ')
#     if inp == 'done': break
#     value = float(inp)
#     numlist.append(value)

# print('Average:', sum(numlist) / len(numlist))


# Lists and strings
# s = 'spam'
# t = list(s)
# print(t)


# s = 'pining for the fjords'
# t = s.split()
# print(t)


# s = 'spam-spam-spam'
# delimiter = '-'
# t = s.split(delimiter)
# print(t)


# t = ['pining', 'for', 'the', 'fjords']
# delimiter = ' '
# result = delimiter.join(t)
# print(result)


#  Parsing lines

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()    
#     if not line.startswith('From '): continue
#     words = line.split()
#     print(words)


t = ['a', 'b', 'c']
x = t.pop(1)

print (x)
print (t)
print(t[0], t[1])