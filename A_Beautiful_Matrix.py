# codeforce
col = 0
row = 0
for r in range(5):
    temp = input().split()
    if '1' in temp:
        col = temp.index('1')
        row = r

print(abs(row-2)+abs(col-2))
