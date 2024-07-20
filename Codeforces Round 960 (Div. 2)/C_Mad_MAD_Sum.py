for i in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]

    ans = arr[0]
    
    
    appear = [0 for i in range(n+10)]
    appear[arr[0]] += 1
    arr[0] = 0
    b = [0 for i in range(n+10)]
    start_idx = n

    for j in range(1,n):
        ans += arr[j]
        appear[arr[j]] += 1
        if appear[arr[j]] > 1:
            arr[j] = max(arr[j] , arr[j-1])
        else:
            arr[j] = arr[j-1]
        b[arr[j]] += 1
        

    last = 0
    more = 0
    #print("DEBUG" , ans)
    #print(arr)

    for j in range(n,0,-1):
        
        if b[j] == 0:
            continue

        
        if b[j] > 1:
            ans += b[j] * j
            b[j] += more
            ans += (last) * b[j] * j 
            more = 0
        elif b[j] == 1:
            more += 1
        ans += ((1+b[j]) * b[j]) // 2 * j
        last += b[j]
    
    print(ans)