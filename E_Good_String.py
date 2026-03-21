# codeforces
# https://codeforces.com/gym/680006/problem/E
n = int(input())
s = input()
res = []

for c in s:
    if len(res) % 2 == 0 or c != res[-1]:
        res.append(c)
    
if len(res) % 2:
    res.pop()

print(n-len(res))
print("".join(res))