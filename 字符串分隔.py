import  sys

s = input().strip()
while(s):
    s1 = s[:8]
    s = s[8:]
    if len(s1)<8:
        s1 = s1 + '0' * ( 8-len(s1))
    print(s1)

s = input().strip()

while s:
    # 取前 8 个
    chunk = s[:8]
    s = s[8:]

    # 如果不足 8 个，补 0
    if len(chunk) < 8:
        chunk = chunk + '0' * (8 - len(chunk))

    print(chunk)
