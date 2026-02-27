# codeforces
t = int(input())
for _ in range(t):
    keyboard = input()

    res = set()
    i = 0
    n = len(keyboard)
    while i < n:
        j = i
        while j < n and keyboard[i] == keyboard[j]:
            j += 1
        
        if (j-i) % 2:
            res.add(keyboard[i]) 
        i = j

    print("".join(sorted(list(res))))