# leetcode
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = {}
        # keep track of the last occurrence each char
        for i in range(len(s)):
            pos[s[i]] = i

        result = []
        max_i = 0
        prev = -1
        # find the max coverage and when i == max coverage element count the elements in that partition
        for i in range(len(s)):
            max_i = max(max_i, pos[s[i]])
            if max_i == i:
                result.append(i - prev)
                prev = max_i
        return result