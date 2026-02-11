# leetcode
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        avg = num//3
        return [avg-1, avg, avg+1] if avg*3==num else []