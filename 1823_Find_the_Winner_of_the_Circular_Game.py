# leetcode
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [n for n in range(1,n+1)]
        cur = 0
        
        while len(players) > 1:
            cur = (cur + k - 1) % len(players) # simulating zero indexing and keeping circular indexing
            players.pop(cur)

        return players[0]
