# leetcode
from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = defaultdict(int)

        for b in bills:
            if b == 5:
                cash[b] += 1
            elif b == 10 and cash[5] > 0:
                cash[b] += 1
                cash[5] -= 1
            elif b == 20 and cash[5] > 0:
                if cash[10] > 0:
                    cash[5] -= 1
                    cash[10] -= 1
                elif cash[5] >= 3:
                    cash[5] -= 3
                else:
                    return False
                cash[b] += 1
            else:
                return False
        return True