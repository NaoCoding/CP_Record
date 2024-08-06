for i in range(int(input())):
    n,k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    one = sum(arr)
    zero = n - one
    
    ans = 0

    o1,z1 = 1 , 1

    start = max((k+1)//2 ,  k - zero)

    for q in range(start):
        o1 *= (one-q)

    for q in range(1,start+1):
        o1 //= q

    for q in range(k-start):
        z1 *= (zero - q)
        
    for q in range(1,k-start+1):
        z1 //= q
    

    ans += z1 * o1
        

    for j in range(start+1 , k + 1):
        
        if j > one:
            break      
        
        

        

        o1 *= (one - j + 1)
        o1 //= j
        
        z1 *= (zero - (k - j - 1))

        if k != j:
            z1 //= k - j
        else:
            z1 = 1

        
        ans += o1*z1
        ans %= (10**9+7)

        #print(ans)
    
    


    print(ans%(10**9+7))
        
