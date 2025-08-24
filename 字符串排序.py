import sys
n = int(input().strip())
str = []
for _ in range(n):
    str.append(input().strip())
for w in sorted(str):
    print(w)