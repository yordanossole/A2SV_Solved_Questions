# leetcode
class Solution:
    def maxScore(self, s: str) -> int:
        # running sum
        score = 0
        left = 0
        total = sum(map(int, s))
        for i in range(len(s)-1):
            left += int(s[i])
            l = i+1 - left
            r = total - left
            score = max(score, l+r)

        return score
        
        # # prifix sum
        # prefix = []
        # cur_sum = 0
        # for n in s:
        #     cur_sum += int(n)
        #     prefix.append(cur_sum)
        
        # score = 0
        # for i in range(len(prefix)-1):
        #     l = i + 1 - prefix[i]
        #     r = prefix[-1] - prefix[i]
        #     score = max(score, l+r)

        # return score