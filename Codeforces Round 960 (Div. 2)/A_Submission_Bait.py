for i in range(int(input())):
    n = int(input())
    q = [int(x) for x in input().split()]
    q.sort()
    idx = -1
    while q.count(q[idx]) % 2 == 0:
        idx -= q.count(q[idx])
        if -idx >= n:
            break
    
    if q.count(q[max(-n , idx)])%2 == 1:
        print("YES")
    else:
        print("NO")
    
