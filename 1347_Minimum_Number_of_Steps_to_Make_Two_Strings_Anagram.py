# leetcode
from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # more optimized:
        s_freq = Counter(s)
        t_freq = Counter(t)
        # the difference shows type and amount of needed characters
        difference = s_freq - t_freq
        return sum(difference.values())
        # dic_s = dict()
        # dic_t = dict()

        # for char in s:
        #     if not char in dic_s.keys():
        #         dic_s[char] = 1
        #     else:
        #         dic_s[char] += 1

        # for char in t:
        #     if not char in dic_t.keys():
        #         dic_t[char] = 1
        #     else:
        #         dic_t[char] += 1

        # # print('s',dic_s)
        # # print('t',dic_t)

        # result = 0

        # for char in list(dic_t.keys()):
        #     if char in list(dic_s.keys()):
        #         dic_t[char] -= dic_s[char]
        #         result += max(0, dic_t[char])
        #         # print('a',result)
        #     else:
        #         result += dic_t[char]
        #         # print('b',result)

        # return result