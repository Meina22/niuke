import  sys

n = int(input().strip())
nums = []
for _ in range(n):
    nums.append(int(input().strip()))
result = sorted(set(nums))
for num in result:
    print(num)