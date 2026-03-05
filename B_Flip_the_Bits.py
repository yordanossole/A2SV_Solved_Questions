# codeforces
t = int(input())
for _ in range(t):
    n = int(input())
    bits1 = list(input())
    bits2 = list(input())

    possible = True
    zeros, ones = 0, 0
    flip_point = [False] * n

    for i in range(n):
        if bits1[i] == "0":
            zeros += 1
        else:
            ones += 1
        if zeros == ones:
            flip_point[i] = True

    for i in range(n-1):
        if (bits1[i] == bits2[i]) != (bits1[i+1] == bits2[i+1]):
            if not flip_point[i]:
                possible = False
                break
    
    if bits1[-1] != bits2[-1] and not flip_point[-1]:
        possible = False

    print("YES" if possible else "NO")