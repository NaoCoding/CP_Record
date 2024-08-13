for i in range(int(input())):
    a = int(input())
    b = [int(x) for x in input().split()]

    q = [0 for i in range(a+1)]

    if b[0] < a: q[b[0]+1] = 1
    if b[0] > 0: q[b[0]-1] = 1
    ok = 1

    for j in b[1:]:
        if q[j] != 1:
            print("NO")
            ok = 0
            break
            
        else:
            if j < a: q[j+1] = 1
            if j > 0: q[j-1] = 1
    if ok == 0:
        continue
    print("YES")
        