# leetcode
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        greater = defaultdict(lambda : -1)
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                greater[stack.pop()] = num
            stack.append(num)
        
        return [greater[num] for num in nums1]

        # # Bruteforce - O(n^2)
        # res = [-1] * len(nums1)
        # nums1_i = {n:i for i,n in enumerate(nums1)}

        # for i in range(len(nums2)):
        #     if not nums2[i] in nums1:
        #         continue
        #     for j in range(i+1, len(nums2)):
        #         if nums2[j] > nums2[i]:
        #             index1 = nums1_i[nums2[i]]
        #             res[index1] = nums2[j]
        #             break
        # return res