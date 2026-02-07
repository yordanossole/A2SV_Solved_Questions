# codeforce
n = int(input())
rating = list(map(int, input().split()))
result = []
for r in rating:
    counter = 0
    for i in rating:
        if r < i:
            counter += 1
    result.append(str(counter+1))
print(" ".join(result))




