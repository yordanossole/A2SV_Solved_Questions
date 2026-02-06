# leetcode
from collections import defaultdict
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        temp = defaultdict(list)
        
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    temp[i+j].append(list1[i])
                    break
        return temp[min(temp)]

        # # the same approach but done years ago
        # dic = dict()
        # for s1 in list1:
        #     if s1 in list2:
        #         indexSum = list1.index(s1) + list2.index(s1)
        #         dic[s1] = indexSum

        # sorted_item = sorted(dic.items(), key = lambda s:s[1])
        # indexSum = [pair[1] for pair in sorted_item]
        # minimum = min(indexSum)
        # result = []
        # for pair in sorted_item:
        #     if pair[1] == minimum:
        #         result.append(pair[0])
        # return result
