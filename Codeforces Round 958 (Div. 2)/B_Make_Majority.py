for i in range(int(input())):
    n = int(input())
    q = list(input())


    idx = 0
    total = 0
    while idx < n:
        if q[idx] == '1':
            total += 1
        elif q[idx] == '0':
            if idx > 0:
                if q[idx-1] == '0':
                    total += 1

            total -= 1
            
        idx += 1
    
    
    
    if total > 0:
        print("Yes")
    else:
        print("No")
    