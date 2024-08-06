for i in range(int(input())):
    n = [1 if j == '1' else -1 for j in input()]
    ans = 0
    
    ff = [0 for j in range(len(n)*2+5)]
    for j in range(len(n)):
        if j:
            n[j] += n[j-1]
        ff[n[j] + len(n)] += 1
    
    #print(ff)

    for j in range(len(n)):
        #print(ff[len(n) - n[j]])
        print(ff[len(n) - (0 if j == 0 else n[j-1])])
        
        if ff[len(n) - (0 if j == 0 else n[j-1])] > 0:

            p = 1

            for k in range(1,ff[len(n) - (0 if j == 0 else n[j-1])]+2):
                p *= k
        
            ans += (p//2)
    
    print(ans)


    
        