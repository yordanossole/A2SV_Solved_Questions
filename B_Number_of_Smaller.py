# codeforces
n, m = list(map(int, input().split()))
first = list(map(int, input().split()))
second = list(map(int, input().split()))

i = 0
result = []

for num in second:
    while i < n and first[i] < num:
        i += 1
    result.append(i)
print(*result)