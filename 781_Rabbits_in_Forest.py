# leetcode
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        seen = {}
        
        for ans in answers:
            if ans in seen:
                if seen[ans] > 0:
                    seen[ans] -= 1
                else:
                    seen[ans] = ans
            else:
                seen[ans] = ans

        return len(answers) + sum(seen.values())