import sys

for i in range(int(input())):

    l,r = 1,1000
    mid = (l+r)//2
    
    while l < r:
        mid = (l+r)//2

        print(f'? {mid} {mid}')
        sys.stdout.flush()

        response = int(input())
        if response == mid * mid:
            l = mid
        else:
            r = mid

    print(f'! {mid}')
    sys.stdout.flush()