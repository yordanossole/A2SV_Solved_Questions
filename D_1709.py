# codeforces
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    opr = []

    while True:
        changed = False

        for i in range(n):
            if a[i] > b[i]:
                opr.append((3, i+1))
                a[i], b[i] = b[i], a[i]
                changed = True
        
        for i in range(n):
            for j in range(n-1):
                if a[j] > a[j+1]:
                    opr.append((1, j+1))
                    a[j], a[j+1] = a[j+1], a[j]
                    changed = True


        for i in range(n):
            for j in range(n-1):
                if b[j] > b[j+1]:
                    opr.append((2, j+1))
                    b[j], b[j+1] = b[j+1], b[j]
                    changed = True

        if not changed:
            break
    
    if len(opr) == 0:
        print(0)
    else:
        print(len(opr))
        for t, i in opr:
            print(t, i)