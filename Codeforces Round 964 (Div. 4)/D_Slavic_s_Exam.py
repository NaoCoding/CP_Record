for i in range(int(input())):
    s = list(input())
    r = list(input())
    idx = 0

    for j in range(len(s)):
        if s[j] == '?' or s[j] == r[idx]:
            s[j] = r[idx]
            idx += 1
            if idx >= len(r):
                break

    for j in range(len(s)):
        if s[j] == '?':
            s[j] = 'a'
    
    if idx == len(r):
        print(f"YES\n{''.join(s)}")
    else:
        print("NO")
    

