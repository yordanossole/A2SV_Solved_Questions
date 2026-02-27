# codeforces
n, s = list(map(int, input().split()))
nums = list(map(int, input().split()))

left = 0
min_len = float('inf')
cur_sum = 0
for right in range(n):
    cur_sum += nums[right]
    while cur_sum - nums[left] >= s:
        cur_sum -= nums[left]
        left += 1
    if cur_sum >= s:
        min_len = min(min_len, right-left+1)

print(min_len if min_len != float('inf') else -1)