import  sys
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    words = line.split()
    print(len(words[-1]))