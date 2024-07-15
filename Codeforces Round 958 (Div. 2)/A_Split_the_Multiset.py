for i in range(int(input())):
    a,b = [int(x) for x in input().split()]
    c = (a-1)//(b-1) + (1 if (a-1)%(b-1) > 0 else 0)
    print(c)