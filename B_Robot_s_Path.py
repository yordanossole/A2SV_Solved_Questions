# codeforces
n, k = list(map(int, input().split()))
road = input()

flag = False
obstacle = 0
for char in road:
    if char == "#":
        obstacle += 1
        if obstacle >= k:
            flag = True
            break
    elif char == ".":
        obstacle = 0

print("NO" if flag else "YES")