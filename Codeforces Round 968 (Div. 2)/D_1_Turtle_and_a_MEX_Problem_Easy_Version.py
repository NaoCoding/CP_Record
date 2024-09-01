for i in range(int(input())):
    n,m = [int(x) for x  in input().split()]

    pp = 1
    ans = 0

    for j in range(n):
        f = [int(x) for x in input().split()]

        if n > m:
            break

        r = sorted(f[1:])
        idx = 1
        t = 0

        while idx < f[0]:
            if r[idx] == r[idx-1] or r[idx] - 1 == r[idx-1]:
                idx += 1
            else:
                t += 1
                if t == 2:
                    pp = max(pp , r[idx] + 1)
                    break

        if t < 2:
            pp = max(pp , f[0])
        
        
        
        

        

    if pp <= m:
        print((1+m)*m // 2 + (1+pp)*pp // 2)
    else:
        print(pp*(m+1))
    
    
        


        