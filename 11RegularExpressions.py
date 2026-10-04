
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     #print(line)
#     #if re.search(r'^From:', line):
#     if re.search(r"\d+", line):
#         print(line)

# Character matching in regular expressions

# Search for lines that start with 'F', followed by
# 2 characters, followed by 'm:'
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^F...', line):
#         print(line)


# Search for lines that start with From and have an at sign
# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search(r'^From:.+@', line):
#         print(line)


# Extracting data using regular expressions

# import re
# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# lst = re.findall(r'\S+@\S+', s) #['csev@umich.edu', 'cwen@iupui.edu']
# print(lst)



# Search for lines that have an at sign between characters
# Search for lines that have an at sign between characters
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall(r'\S+@\S+', line)
    if len(x) > 0:
        print(x)


