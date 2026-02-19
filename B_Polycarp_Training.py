# codeforces
n = int(input())
contests = list(map(int, input().split()))
contests.sort()
day = 1
for prob in contests:
    if prob >= day:
        day += 1

print(day-1)