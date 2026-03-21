# codeforces
# https://codeforces.com/gym/680006/problem/C
a, b = list(map(int, input().split()))
steps = [b]

while a < b:
    if str(b)[-1] == "1":
        b //= 10
    elif b % 2 == 0:
        b //= 2
    else:
        break
    steps.append(b)

if a == b:
    print("YES")
    print(len(steps))
    steps.sort()
    print(*steps)
else:
    print("NO")