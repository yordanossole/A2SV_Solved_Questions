# leetcode
from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = Counter()
        for winner, loser in matches:
            winners.add(winner)
            losers[loser] += 1
        
        ans1 = []
        ans2 = []

        for player, count in losers.items():
            if count == 1:
                ans2.append(player)
        
        for player in winners:
            if not player in losers:
                ans1.append(player)
        
        ans1.sort()
        ans2.sort()

        return [ans1, ans2]
