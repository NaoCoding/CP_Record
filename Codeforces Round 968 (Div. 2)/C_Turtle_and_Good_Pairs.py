for i in range(int(input())):
    n = int(input())
    f = list(input())
    
   
    while len(f):

        appear = [0 for j in range(150)]
        idx = 0

        while idx < len(f):
            
            if appear[ord(f[idx])] == 1:
                idx += 1
                continue

            appear[ord(f[idx])] = 1
            print(f.pop(idx), end = "")

            



        
    
    print()