# codeforces
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    deck = list(map(int, input().split()))

    deck.sort()
    l = 0
    max_deck = 0
    for r in range(0,n):
        if r > 0 and deck[r] > deck[r-1] + 1: # if invalid
            l = r

        while deck[r] - deck[l] + 1 > k: # unique numbers
            l += 1

        max_deck = max(max_deck, r - l + 1)
        
    print(max_deck)