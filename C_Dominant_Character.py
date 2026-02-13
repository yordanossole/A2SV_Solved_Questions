# codeforce
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    ans = -1
    possibility = ['aa','aba','aca','abca','acba','abbacca','accabba']
    for pos in possibility:
        if pos in s:
            ans = len(pos)
            break

    print(ans)
