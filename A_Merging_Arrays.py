# codeforces
n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

f, s = 0, 0
result = []
while f < n and s < m:
    if arr1[f] < arr2[s]:
        result.append(arr1[f])
        f += 1
    else:
        result.append(arr2[s])
        s += 1

result.extend(arr1[f:])
result.extend(arr2[s:])

[print(i, end=" ") for i in result]