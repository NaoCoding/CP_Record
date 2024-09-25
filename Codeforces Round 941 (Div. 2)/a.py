for i in range(int(input())):
    n,k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    p = [0 for i in range(101)]
    for j in arr:
        p[j] += 1
    
    while(max(p) >= k):
        p[p.index(max(p))] -= k
        p[p.index(max(p))] += k - 1
    
    print(sum(p))