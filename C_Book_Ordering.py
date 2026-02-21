# codeforces
n = int(input())
books = []
for _ in range(n):
    book = list(map(int, input().split()))
    books.append(book)

found = False
lead = max(books[0])
for book in books:
    book.sort(reverse=True)
    for height in book:
        if height <= lead:
            lead = height
            found = True
            break
    else:
        found = False
        break
    
print("YES" if found else "NO")