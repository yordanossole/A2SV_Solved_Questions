# codeforces
n = int(input())
levels = list(map(int, input().split()))

factorial = 0
for i in range(n,0,-1):
    factorial += i

print(factorial - sum(levels))