# codeforces
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))

    casino = []
    for _ in range(n):
        c = tuple(map(int, input().split()))
        casino.append(c)
    
    casino.sort()
    
    for L, r, real in casino:
        if L<=k<=r and real > k:
            k = real
    print(k)