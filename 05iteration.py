# x=5;     # None
# x=x+1
# print(x)


## while loop
# n = 5
# while n > 0:
#     n -= 1
#     print(n)
# print('Blastoff!')


# n=10
# while True:
#     print(n, sep=' \t',end=' ')
#     n = n - 1
#     if n == 0:
#         break
# print('Done!')

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')


#friends = ['Joseph', 'Glenn', 'Sally']
# friends = {'Joseph':1, 'Glenn':2, 'Sally':3}
# for friend in friends:
#     print('Happy New Year:', friends[friend])

# print('Done!')

# for friend in ['Joseph', 'Glenn', 'Sally']:
#     print('Happy New Year:', friend)


# count = 0
# for iterval in [3, 41, 12, 9, 74, 15]:
#     print(iterval)
#     count = count + 1
# print('Count: ', count)

# total = 0
# for iterval in [3, 41, 12, 9, 74, 15]:
#     total = total + iterval
#     print(total)
# print('Total: ', total)


# largest = None
# print('Before:', largest)
# for iterval in [3, 41, 12, 9, 74, 15]:
#     if largest is None or iterval > largest:
#         largest = iterval
#         print('Loop:', iterval, largest)
# print('Largest:', largest)

# smallest = None
# print('Before:', smallest)
# for iterval in [3, 41, 12, 9, 74, 15]:
#     if smallest is None or iterval < smallest:
#         smallest = iterval
#     print('Loop:', iterval, smallest)

# print('Smallest:', smallest)


def min_method(values):
    smallest = None
    for value in values:
        if smallest is None or value < smallest:
            smallest = value
    return smallest

print(min_method([7, 2, 3, 4, 5])) #2