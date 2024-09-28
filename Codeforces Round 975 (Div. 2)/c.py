import math

for i in range(int(input())):
    a,coin = [int(x) for x in input().split()]
    n = [int(x) for x in input().split()]
    p = max(n)
    total = sum(n)
    q = a*p - total
    if coin >= q:
        print(min(a , coin + total))

    else:
        if total % p == 0 or p - total % p <= coin:
            print((total+coin)//p)
        else:
            print(min((total+coin - (total+coin)%p)//p , 
                      (total+coin - (total+coin)%a)//a))



        

