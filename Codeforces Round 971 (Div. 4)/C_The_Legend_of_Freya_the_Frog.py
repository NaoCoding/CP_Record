for i in range(int(input())):
    a,b,c = [int(x) for x in input().split()]
    ans = 0
    while a > 0 or b > 0:
        a -= c
        ans += 1
        if a <= 0 and b <= 0:
            break
        b -= c
        ans += 1
    print(ans)