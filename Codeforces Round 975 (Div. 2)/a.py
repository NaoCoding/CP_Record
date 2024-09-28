for i in range(int(input())):
    n = int(input())
    r = [int(x) for x in input().split()]
    ans = [0,0]
    for j in range(n):
        ans[j%2] = max(ans[j%2] , r[j])
    
    if ans[0] + (n+1) // 2 > ans[1] + (n)//2:
        print(ans[0] + (n+1)//2)
    else:
        print(ans[1] + (n)//2)