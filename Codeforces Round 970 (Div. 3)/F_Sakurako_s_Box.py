def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


for i in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]

    if n == 1:
        print(a[0])
        continue

    a.sort(reverse = True)
    now = 0

    for j in range(1 , n):
        now += a[j] * a[0]

    ans = now 

    for j in range(1 , n):
        if a[j] == 0:
            break
        now -= a[j]*a[j-1]
        now = now // a[j-1] * a[j]
        ans += now
    
    err, x , y = egcd((n*(n-1)//2) , (10**9+7))
    
    print(ans * (x)%(10**9+7))
        
    
        
