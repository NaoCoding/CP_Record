for i in range(int(input())):
    l,r = [int(x) for x in input().split()]

    now = 1

    while 3**now <= l:
        now += 1
    
    ans = now
    
    for j in range(l,r+1):
        if 3**now <= j:
            now += 1
        ans += now
        
    
    print(ans)
    
    


    

    