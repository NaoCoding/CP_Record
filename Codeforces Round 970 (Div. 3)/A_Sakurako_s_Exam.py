for i in range(int(input())):
    a,b = [int(x) for x in input().split()]
    if (a%2 == 0 and a > 0) or (a == 0 and b % 2 == 0):
        print("YES")
    else:
        print("NO")
    