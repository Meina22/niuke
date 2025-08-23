import sys
from collections import defaultdict
data = defaultdict(int)
n = int(input().strip())
for _ in range(n):
    index ,val = map(int,input().split())
    data[index] += val
for index in sorted(data):
    print(index,data[index])
