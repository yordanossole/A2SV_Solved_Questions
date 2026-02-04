# codeforce
s, n = map(int, input().split(" "))
game = []
for _ in range(n):
    a, b = map(int, input().split(" "))
    game.append((a,b))

game.sort()

for dragon_s, reward in game:
    if s <= dragon_s:
        print("NO")
        break
    s += reward
else:
    print("YES")