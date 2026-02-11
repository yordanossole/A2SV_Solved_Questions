# leetcode
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        total = sum(x for x in nums if x%2 == 0)
        for val, index in queries:
            old = nums[index]
            new = old + val
            
            # always minus even old values
            if old % 2 == 0: 
                total -= old

            if new % 2 == 0:
                total += new
                
            nums[index] = new
            answer.append(total)

        return answer