# hackerrank
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phone_book = {}
for _ in range(n):
    name, num = input().split(" ")
    phone_book[name] = num

while True:
    try:
        name = input()
        if name in phone_book:
            num = phone_book[name]
            print(f"{name}={num}") 
        else:
            print("Not found")
    except Exception:
        break
    