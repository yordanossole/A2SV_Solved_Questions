# leetcode
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill)-1
        total = skill[left] + skill[right]
        result = 0
        while left < right:
            cur_sum = skill[left] + skill[right]
            if cur_sum != total:
                return -1
            result += skill[left] * skill[right]
            left += 1
            right -= 1
        return result