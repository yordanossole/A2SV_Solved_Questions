# codeforce
from collections import Counter
n = int(input())
for _ in range(n):
    s, t, p = [list(input()) for _ in range(3)]

    p_c = Counter(p)
    left, right = 0, 0

    while left < len(s) and right < len(t):
        if s[left] == t[right]:
            left += 1
            right += 1
        elif p_c[t[right]] > 0:
            p_c[t[right]] -= 1
            right += 1
        else:
            break
    
    while right < len(t) and p_c[t[right]] > 0:
        p_c[t[right]] -= 1
        right += 1

    if left == len(s) and right == len(t):
        print("YES")
    else:
        print("NO")
