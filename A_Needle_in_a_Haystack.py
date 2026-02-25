# codeforces
from collections import Counter
t = int(input())
for _ in range(t):
    s = input()
    t = input()
    t_counts = Counter(t)
    s_counts = Counter(s)

    if not s_counts <= t_counts:
        print("Impossible")
        continue

    result = []
    keys = sorted(t_counts.keys())
    s_pointer = 0

    for _ in range(len(t)):
        for char in keys:
            if t_counts[char] > 0:
                if s_pointer < len(s) and s[s_pointer] == char:
                    result.append(char)
                    t_counts[char] -= 1
                    s_counts[char] -= 1
                    s_pointer += 1
                    break
                else:
                    # check we have enough char in t_counts to form s before adding the remaining
                    t_counts[char] -= 1
                    if s_counts <= t_counts:
                        result.append(char)
                        break
                    else:
                        t_counts[char] += 1

    print("".join(result))