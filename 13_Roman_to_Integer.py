# leetcode
class Solution:
    def romanToInt(self, s: str) -> int:
            dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
            result = 0
            
            for i in range(len(s)):
                if i+1 < len(s) and dic[s[i]] < dic[s[i+1]]:
                    result -= dic[s[i]]
                else:
                    result += dic[s[i]]

            return result

            # result = 0
            # prev = 0

            # for char in reversed(s):
            #     cur = dic[char]
            #     if cur < prev:
            #         result -= dic[char]
            #     else:
            #         result += dic[char]
            #     prev = cur
            # return result