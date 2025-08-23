# import sys
# s = input().strip()
# c = input().strip()
#
# count = 0
# if c.isdigit():
#     for ch in s:
#         if c == ch:
#             count+=1
# elif c.isalpha():
#     for ch in s:
#         if c.lower() == ch.lower():
#             count+=1
# print(count)


import sys
s = input().strip()
c = input().strip()

count = 0
if c.isalpha():
    for ch in s:
        if ch.lower() == c.lower():
            count+=1
elif c.isdigit():
    for ch in s:
        if ch == c:
            count+=1
print(count)