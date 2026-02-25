# codeforces
n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

total = nums[-1] - nums[0]
dif = []
for i in range(0, n-1):
    dif.append(nums[i+1] - nums[i])

dif.sort(reverse=True)
print(total-sum(dif[:k-1]))