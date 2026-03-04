# codeforces
n, s = list(map(int, input().split()))
nums = list(map(int, input().split()))

counter, left, cur_sum = 0, 0, 0
for right in range(n):
    cur_sum += nums[right]

    while cur_sum > s and left <= right:
        cur_sum -= nums[left]
        left += 1
    
    counter += right - left + 1

print(counter)