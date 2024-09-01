import math
for i in range(int(input())):
    l,r = [int(x) for x in input().split()]
    pos = r - l + 1
    print(int(math.sqrt(pos*2) + 0.5))