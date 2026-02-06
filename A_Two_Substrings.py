# codeforce
def helper(word, flag):
    first = "AB" if flag == True else "BA"
    second = "BA" if flag == True else "AB"

    index = word.find(first)
    if index == -1:
        return False
    
    left = word[:index]
    right = word[index+2:]
    if left.find(second) != -1:
        return True
    if right.find(second) != -1:
        return True
    
    return False

def solve():
    word = input()
    can = helper(word, True) or helper(word, False)
    if can:
        print("YES")
    else:
        print("NO")

solve()