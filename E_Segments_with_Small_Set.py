# codeforces
from collections import defaultdict
n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

counter = defaultdict(int)
result = 0
left = 0
for right in range(n):
    if counter[nums[right]] == 0:
        k -= 1

    counter[nums[right]] += 1

    while k < 0:
        counter[nums[left]] -= 1
        if counter[nums[left]] == 0:
            k += 1
        left += 1

    result += right - left + 1

print(result)