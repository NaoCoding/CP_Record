for i in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    color = [int(x) for x in list(input())]
    ans = [-1 for j in range(n)]

    for j in range(n):
        if ans[j] != -1:
            continue

        st = [j]
        b = 1 - color[j]

        ne = a[j] - 1

        while ne != st[0]:
            b += 1 - color[ne]
            st.append(ne)
            ne = a[ne] - 1
        
        for k in range(len(st)):
            ans[st[k]] = b
    
    for j in range(n):
        print(ans[j] , end = " ")
    print()