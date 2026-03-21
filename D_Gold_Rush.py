# codeforces
# https://codeforces.com/gym/680006/problem/D
import sys
sys.setrecursionlimit(10**7)

t = int(input())
def reach(current, target):
    if current == target:
        return True
    if current % 3 != 0 or current < target:
        return False

    return reach(current // 3, target) or reach(2 * current // 3, target)

for _ in range(t):
    n, m = map(int, input().split())

    if reach(n, m):
        print("YES")
    else:
        print("NO")