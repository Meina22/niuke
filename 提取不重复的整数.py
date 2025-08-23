import sys
s = input().strip()
s = s[::-1]
count = [0]*10
n = len(s)
result = []
for i in range(n):
    if count[int(s[i])] ==0:
        count[int(s[i])]+=1
        result.append(s[i])
print(''.join(result))


