import math
for i in range(int(input())):
    n = int(input())
    s = list(input())

    zeros = s.count('0')

    pos = 0
    #print(zeros)

    for j in range(1 , n//2 + 1):
        if n%j != 0 or (j*2 + n//j * 2 - 4 + zeros != n) or j*j != n:
            continue
        else:
            temp = 1
            for k in range(0 , j):
                if s[k] != '1':
                    temp = 0
                    break
            if temp == 0:
                continue
            
            for k in range(0 , n , j):
                if s[k] != '1':
                    temp = 0
                    break
            if temp == 0:
                continue
                
            for k in range(j - 1 , n  , j):
                if s[k] != '1':
                    temp = 0
                    break
            if temp == 0:
                continue
            
            for k in range(n - j , n  , 1):
                if s[k] != '1':
                    temp = 0
                    break
            if temp == 1:
                #print(j)
                pos = 1
                break
    if pos == 1:
        print("Yes")
    else:
        print("No")

