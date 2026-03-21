# codeforces
# https://codeforces.com/gym/680006/problem/A
k = int(input())
finalist = list(map(int, input().split()))

additionals = [] # mono decrease
for i in range(k):
    if finalist[i] > 25:
        additionals.append(finalist[i])

additionals.sort(reverse=True)
dif = 0
if additionals:
    for i in range(len(additionals)-1):
        dif += (additionals[i] - additionals[i+1])
    dif += (additionals[-1] - 25)

print(dif)