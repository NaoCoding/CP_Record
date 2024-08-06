for i in range(int(input())):
    a = [int(x) for x in input().split()]
    
    ans = 0
    if a[0] > a[2] and a[1] > a[3]:
        ans += 1
    if a[0] > a[3] and a[1] > a[2]:
        ans += 1
    if a[0] > a[2] and a[1] == a[3]:
        ans += 1
    if a[0] > a[3] and a[1] == a[2]:
        ans += 1
    if a[1] > a[3] and a[0] == a[2]:
        ans += 1
    if a[1] > a[2] and a[0] == a[3]:
        ans += 1


    print(ans * 2)


    

    
    
    

    
    