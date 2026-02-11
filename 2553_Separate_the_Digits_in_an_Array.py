# leetcode
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            answer.extend(list(map(int, str(num))))
        return answer
        