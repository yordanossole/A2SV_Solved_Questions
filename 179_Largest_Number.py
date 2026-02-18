# leetcode
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strings = [str(num) for num in nums]

        for i in range(len(strings)):
            for j in range(i+1, len(strings)):
                if int(strings[i]+strings[j]) < int(strings[j]+strings[i]):
                    strings[i], strings[j] = strings[j], strings[i]
        
        result = "".join(strings)
        if int(result) == 0:
            return "0"

        return result