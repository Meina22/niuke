import sys
n = int(input().strip())
s = bin(n)[2:]
count=0
for i in range(len(s)):
    if s[i]=='1':
        count+=1
print(count)