for i in range(int(input())):
    n = int(input())
    l = [input() for j in range(n)]
    for k in l[::-1]:
        print(k.index("#") + 1,end = " ")
    print()