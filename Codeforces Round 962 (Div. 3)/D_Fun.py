import math
for i in range(int(input())):
    n,x = [int(_) for _ in input().split()]
    
    ans = 0

    for j in range(1,int(math.sqrt(n)) + 1):
        for k in range(j,int(math.sqrt(n)) + 1):
            if k > x - j - k:
                break
            if j == k:
                ans += 4
            else:
                ans += 1
            
            ans += (min(x-j-k , 1 + 2*(x-j-k))-k-1) * 6
            
            
            
            
            
            
            
            
            

    print(ans)


