for i in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()

    print(a[n//2])
