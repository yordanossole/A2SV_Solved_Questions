# codeforces
from collections import Counter
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    paper = input()

    counter = Counter(paper[:k])
    result = counter["W"]

    for r in range(k,n):
        counter[paper[r]] += 1
        counter[paper[r-k]] -= 1
        result = min(result, counter["W"])
    
    print(result)