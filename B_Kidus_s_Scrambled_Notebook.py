# codeforce
n = int(input())
for _ in range(n):
    num = input()
    for pointer in range(1, len(num)):
        
        if num[pointer:][0] == '0':
            continue
        
        a = int(num[:pointer])
        b = int(num[pointer:])
        if a > 0 and b > 0 and b > a:
            print(a, b)
            break
    else:
        print(-1)
