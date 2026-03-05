# codeforces
n, k, q = list(map(int, input().split()))
books = []

diff = [0] * 200005
for _ in range(n):
    l, r = list(map(int, input().split()))
    diff[l] += 1 
    diff[r + 1] -= 1

over_lap = [0] * 200005
run_sum = 0
for i in range(1, 200001):
    run_sum += diff[i]
    over_lap[i] = 1 if run_sum >= k else 0
    over_lap[i] = over_lap[i-1] + over_lap[i]

for _ in range(q):
    a, b = list(map(int, input().split()))
    print(over_lap[b] - over_lap[a-1])