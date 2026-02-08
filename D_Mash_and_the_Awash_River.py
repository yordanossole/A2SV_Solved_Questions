# codeforce
n = int(input())
for i in range(n):
    left = 0
    right = 0
    cells = input()

    # checking infinit conditions
    if ">*" in cells or "*<" in cells or "**" in cells or "><" in cells:
        print(-1)
        continue

    # counting < and > independently and add one on both if *
    for c in cells:
        if c == "<":
            left += 1
        elif c == "*":
            left += 1
            right += 1
        elif c == ">":
            right += 1
    print(max(left, right))
