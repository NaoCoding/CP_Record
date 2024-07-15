for i in range(int(input())):
    n = bin(int(input()))
    answer = [n]
    p = len(answer)
    target = 0
    idx = -1
    f = 1
    while target < int(answer[0] , 2):
        target = (int(answer[0], 2) | int(n, 2) ) -  (int(answer[0], 2) & int(n, 2)) 
        
        if target > int(answer[0] , 2):
            break

        
        
        while answer[0][idx] == '0':
            idx -= 1
            f *= 2
            if answer[0][idx] == 'b':
                break
        
        if int(answer[0], 2) - f + target <= 0:
            break

        answer.insert(0 , bin(int(answer[0], 2) - f + target))
       
        
    
    print(len(answer))
    for j in answer:
        print(int(j , 2) , end = ' ')
    print()


        