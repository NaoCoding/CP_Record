for i in range(int(input())):
    n = int(input())
    val = [int(x) for x in input().split()]
    qr = [None for x in range(n)]
    pairs = []

    if n == 1:
        print(val[0])
        continue

    for j in range(n-1):
        a , b = [int(x) for x in input().split()]

        if qr[a-1] == None and qr[b-1] == None:
            pairs.append([[a-1] , [b-1]])
            qr[a-1] = [len(pairs) - 1 , 0]
            qr[b-1] = [len(pairs) - 1 , 1]
        elif qr[a-1] != None and qr[b-1] == None:
            pairs[qr[a-1][0]][1 - qr[a-1][1]].append(b-1)
            qr[b-1] = [qr[a-1][0] , 1 - qr[a-1][1]]
        elif qr[b-1] != None and qr[a-1] == None:
            pairs[qr[b-1][0]][1 - qr[b-1][1]].append(a-1)
            qr[a-1] = [qr[b-1][0] , 1 - qr[b-1][1]]
        else:
            if qr[a-1][0] < qr[b-1][0]:
                
                s , t = qr[b-1][0] , qr[b-1][1]

                for j in pairs[qr[b-1][0]][qr[b-1][1]]:
                    pairs[qr[a-1][0]][1 - qr[a-1][1]].append(j)
                    qr[j] = [qr[a-1][0] , 1 - qr[a-1][1]]

                

                for j in pairs[s][1-t]:
                    pairs[qr[a-1][0]][qr[a-1][1]].append(j)
                    qr[j] = [qr[a-1][0] , qr[a-1][1]]
                
                
                 
            else:
                s , t = qr[a-1][0] , qr[a-1][1]

                for j in pairs[qr[a-1][0]][qr[a-1][1]]:
                    pairs[qr[b-1][0]][1 - qr[b-1][1]].append(j)
                    qr[j] = [qr[b-1][0] , 1 - qr[b-1][1]]

                

                for j in pairs[s][1-t]:
                    pairs[qr[b-1][0]][qr[b-1][1]].append(j)
                    qr[j] = [qr[b-1][0] , qr[b-1][1]]

    ans = [0,0]
    #print(pairs)
    for j in range(2):
        for k in range(len(pairs[0][j])):
            ans[j] += val[pairs[0][j][k]]
    if ans[0] > ans[1]:
        print(ans[0] + ans[1] * 2)
    else:
        print(ans[0] * 2 + ans[1])
