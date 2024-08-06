for i in range(int(input())):
    n,s,m = [int(x) for x in input().split()]
    ans = 0
    last = 0
    for k in range(n):
        l,r = [int(x) for x in input().split()]
        if l - last >= s:
            ans = 1
        last = r
    if m - last >= s:
        ans = 1
    if ans == 1:
        print("YES")
    else:
        print("NO")