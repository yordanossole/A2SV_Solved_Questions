# codeforces
t = int(input())
for _ in range(t):
    n = int(input())
    per = list(map(int, input().split()))

    result = [per[0]]

    for i in range(1, n-1):
        if per[i-1] > per[i] < per[i+1] or per[i-1] < per[i] > per[i+1]:
            result.append(per[i])

    result.append(per[-1])

    print(len(result))
    print(*result)