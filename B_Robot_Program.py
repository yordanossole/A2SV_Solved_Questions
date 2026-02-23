# codeforces
t = int(input())

for _ in range(t):
    n, x, k = list(map(int, input().split()))
    commands = input()

    first_occurence = -1
    point = x
    for i in range(min(n,k)):
        point += 1 if commands[i] == "R" else -1
        
        if point == 0:
            first_occurence = i + 1
            break
    
    if first_occurence == -1:
        print(0)
        continue

    reset_point = -1
    point = 0 # start after it already became 0
    for i in range(n):
        point += 1 if commands[i] == "R" else -1

        if point == 0:
            reset_point = i + 1
            break
    
    ans = 1
    remaining = k - first_occurence
    if reset_point != -1:
        ans += remaining // reset_point # how many times command is reseted in rest of the list
    print(ans)