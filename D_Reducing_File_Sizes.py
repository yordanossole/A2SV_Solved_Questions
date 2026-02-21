# codeforces
n, m = list(map(int, input().split()))

normal_sum = 0
difference = []

for _ in range(n):
    a, b = list(map(int, input().split()))
    normal_sum += a
    difference.append(a-b)

difference.sort(reverse=True)

flag = False
counter = 0

if normal_sum <= m:
    flag = True
else:
    for dif in difference:
        normal_sum -= dif
        counter += 1
        if normal_sum <= m:
            flag = True
            break

if not flag:
    print(-1)
else:
    print(counter)