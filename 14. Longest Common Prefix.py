class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        temp = sorted(strs)
        first = temp[0]
        last = temp[-1]

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        
        return ans