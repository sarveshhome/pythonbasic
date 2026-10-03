# list -> [] - mutable
# Dictionaries -> {} - mutable
# tuple -> (). - immutable

# t = ('a', 'b', 'c', 'd', 'e')
# print   (t)
# #t[2] = 'x'  
# t = ('Z',) + t[1:]
# print(t)

# Comparing tuples
#print(('1', 3, 'c',6) < ('1', 3, '4',7))


# txt = 'but soft what light in yonder window breaks'
# words = txt.split()
# t = list()
# for word in words:
#     t.append((len(word), word))

# t.sort(reverse=True)
# res = list()
# print('Sorted tuple:', t)


# for length, word in t:
#     res.append((word))

# print(res)


# Tuple assignment

# m =('have', 'a', 'nice', 'day')
# x,y,z,w = m

# print(x)
# print(y)
# print(z)
# print(w)

# addr = 'monty@python.org'
# uname, domain = addr.split('@')
# print(uname)
# print(domain)

# Dictionaries and tuples

# d = {'b':1, 'a':10, 'c':22}
# t = list(d.items())
# print(d.items())
# print(t)

# t.sort() #sort
# print(t)

# Multiple assignment with dictionaries

# d = {'a':10, 'b':1, 'c':22}
# for key, val in d.items():
#     print(val, key)

# The most common words

# import string
# fhand = open('mbox.txt')
# counts = dict()
# for line in fhand:
#     line = line.translate(str.maketrans('', '', string.punctuation))
#     line = line.lower()
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1

# # Sort the dictionary by value
# lst = list()
# for key, val in list(counts.items()):
#     lst.append((val, key))

# lst.sort(reverse=True)
# for key, val in lst[:10]:
#     print(val, key)


# # Using tuples as keys in dictionaries
# number = {}

# # Add records
# number["Kumar", "Sarvesh"] = "9876543210"
# number["Singh", "Rahul"] = "9876543211"
# number["Sharma", "Amit"] = "9876543212"
# print(number)

# for last, first in number:
#     print(first, last, number[last, first])


# List comprehension
# list_of_ints_in_strings = ['42', '65', '12']
# list_of_ints = []
# for x in list_of_ints_in_strings:
#     list_of_ints.append(int(x))
# print(sum(list_of_ints))


list_of_ints_in_strings = ['42', '65', '12']
list_of_ints = [ int(x) for x in list_of_ints_in_strings ]
print(sum(list_of_ints))