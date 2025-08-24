import sys
s = input().strip()
count = 0
visited = []
for i in range(len(s)):
    if ord(s[i]) in visited:
        continue
    elif 0<=ord(s[i])<=127:
        count+=1
        visited.append(ord(s[i]))
print(count)