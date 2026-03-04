# codeforces
from collections import Counter
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_c = Counter(a)
b_c = Counter(b)
p1, p2 = 0, 0
counter = 0

while p1 < n and p2 < m:
    if a[p1] == b[p2]:
        count1 = a_c[a[p1]]
        count2 = b_c[b[p2]]
        counter += count1 * count2
        
        p1 += count1
        p2 += count2
    elif a[p1] < b[p2]:
        p1 += 1
    else:
        p2 += 1

print(counter)