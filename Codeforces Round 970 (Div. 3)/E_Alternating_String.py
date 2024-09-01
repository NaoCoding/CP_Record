for i in range(int(input())):
    n = int(input())
    st = list(input())

    if n == 1:
        print(1)
        continue

    if n % 2 == 0:
        appear = [[0 for k in range(256)] for j in range(2)]
        for j in range(2):
            for k in range(j, n, 2):
                appear[j][ord(st[k])] += 1
        print(n - max(appear[1]) - max(appear[0]))
        continue

    ans = n

    a1 = [[0 for k in range(256)] for j in range(2)]
    a2 = [[0 for k in range(256)] for j in range(2)]

    for j in range(n):
        a2[j%2][ord(st[j])] += 1

    for j in range(n):
        if j > 0:
            a1[(j-1)%2][ord(st[j-1])] += 1
        a2[j%2][ord(st[j])] -= 1
        a3 = [[a1[j][k] + a2[1-j][k] for k in range(256)] for j in range(2)]
        ans = min(ans , n - max(a3[0]) - max(a3[1]))
    print(ans)


    
    
    
        


