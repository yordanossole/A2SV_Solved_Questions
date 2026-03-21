# codeforces
# https://codeforces.com/gym/680006/problem/F
from collections import deque
n, k = map(int, input().split())
h = list(map(int, input().split()))

max_dq = deque()
min_dq = deque()

left = 0
max_len = 0
results = []

for right in range(n):
    while max_dq and h[max_dq[-1]] <= h[right]:
        max_dq.pop()
    max_dq.append(right)

    while min_dq and h[min_dq[-1]] >= h[right]:
        min_dq.pop()
    min_dq.append(right)

    while h[max_dq[0]] - h[min_dq[0]] > k:
        left += 1
        if max_dq[0] < left:
            max_dq.popleft()
        if min_dq[0] < left:
            min_dq.popleft()
    
    current_l = right - left + 1

    if current_l > max_len:
        max_len = current_l
        results = [[left + 1, right + 1]]
    elif current_l == max_len:
        results.append([left + 1, right + 1])
    
    
print(f"{max_len} {len(results)}")
for start, end in results:
    print(f"{start} {end}")