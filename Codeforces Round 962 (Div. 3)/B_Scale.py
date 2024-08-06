for i in range(int(input())):
    a , b = [int(x) for x in input().split()]
    g = [ list(input()) for x in range(a)]
    ans = [[0 for x in range(a//b)] for j in range(a//b)]
    for j in range(a//b):
        for k in range(a//b):
            ans[j][k] = g[int(j*b)][int(k * b)]
    for j in ans:
        print("".join(j))
    