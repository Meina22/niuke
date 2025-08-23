import sys
s = input().strip()
if '.' in s:
    nums = s.split(".")
    num1 = int(nums[0])
    num2 = nums[1]
    n = int(num2[0])
    if n >= 5:
        print(num1 + 1)
    else:
        print(num1)
else:
    print(int(s))

