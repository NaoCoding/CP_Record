for i in range(int(input())):
    n , x , y = [int(x) for x in input().split()]
    ans = [1 for j in range(n)]
    
    xx , yy = n , 0
    while yy < y-1:
        ans[yy] = -1
        yy += 1
    ans[x-1] = 1

    
    for j in range(n):
        print(ans[j] , end=" ")
    print()


