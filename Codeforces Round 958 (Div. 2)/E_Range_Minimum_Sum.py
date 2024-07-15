for i in range(int(input())):
    n = int(input())
    q = input().split()

    if n == 1:
        print(0)
        continue

    num = [int(x) for x in q]

    dp = [[n+1 for j in range(n)] for k in range(n)]

    for j in range(n):
        dp[j][j] = num[j]
    
    for k in range(n):
        for j in range(k-1 , -1 , -1):
            dp[j][k] = min(dp[j+1][k] , num[j])

   

    for j in range(n):
        ans = 0
        for k in range(0 , j):
            for l in range(k , j):
                ans += dp[k][l]
            for l in range(j+1,n):
                ans += min(dp[k][j-1] , dp[j+1][l])

        for k in range(j+1,n):
            for l in range(k , n):
                ans += dp[k][l]
        print(ans, end=" ")
    print()