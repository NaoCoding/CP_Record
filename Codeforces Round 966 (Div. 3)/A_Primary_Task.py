for i in range(int(input())):
    a = input()
    if len(a) < 3:
        print("NO")
    elif a[0] == '1' and a[1] == '0':
        
        if a[2] == '0':
            print("NO")
        else:
            if int(a[2:]) > 1:
                print("YES")
            else:
                print("NO")
    else:
        print("NO")