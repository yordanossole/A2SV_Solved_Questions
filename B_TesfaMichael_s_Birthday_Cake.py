# codeforces
# https://codeforces.com/gym/680006/problem/B
n, k = list(map(int, input().split()))
layers = list(input())

def is_valid(b, a):
    if ord(b) - ord(a) < 2:
        return False
    return True
layers.sort()
stack = [layers[0]]
res = ord(layers[0]) - ord("a") + 1
l = k
for i in range(1, n):
    a = stack[-1]
    b = layers[i]

    if is_valid(b, a) and l > 1:
        l -= 1
        res += (ord(b) - ord("a") + 1)
        stack.append(b)

if len(stack) == k:
    print(res)
else:
    print(-1)