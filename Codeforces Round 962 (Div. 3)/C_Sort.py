for i in range(int(input())):
    a , b = [int(x) for x in input().split()]
    s1 = list(input())
    s2 = list(input())

    ans = [[0 for j in range(27)] for k in range(a+1)]
    f = [0 for k in range(27)]
    


    for j in range(1,a+1):
        f[ord(s1[j-1]) - ord('a')] += 1
        f[ord(s2[j-1]) - ord('a')] -= 1

        for k in range(27):
            ans[j][k] = f[k]
            
 
    for j in range(b):
        l,r = [int(x) for x in input().split()]

        
        reply = 0
        #print(ans[r] , ans[l])
        for k in range(27):
            reply += abs(ans[r][k] - ans[l-1][k])
                

            
        print(reply // 2)