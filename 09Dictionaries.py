# eng2sp = dict()
# print(eng2sp) #[]

# eng2sp['one'] = 'uno'
# print(eng2sp)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
eng2sp['three'] = 'cuatro'
print(eng2sp)
print(type(eng2sp))

# print(eng2sp['two'])

# print(len(eng2sp))

# print('one' in eng2sp)

# vals = list(eng2sp.values())
# print('uno' in vals)
# print(vals)


# word = 'Rakeshkumar'
# d = dict()
# for c in word:
#     if c not in d:
#         d[c] = 1
#     else:
#         d[c] = d[c] + 1
# print(d)


# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# print(counts.get('jans',7))

# word = 'Rakeshkumar'
# d = dict()
# for c in word:
#     d[c] = d.get(c,0) + 1
# val =list(d.values())
# print(val[1])


# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()

# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1

# print(counts)

# Looping and dictionaries

# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for i in counts:
#     print(counts[i])


# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for key in counts:
#     if counts[key] > 10:
#         print(key, counts[key])


# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# lst = list(counts.values())
# print(lst)
# lst.sort()
# print(lst)

# for value in lst:
#   for key, val in counts.items():
#     if val == value:
#         print(key, value)


# Advanced text parsing 

