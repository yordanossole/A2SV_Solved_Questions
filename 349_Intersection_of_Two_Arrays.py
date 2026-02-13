# leetcode
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
        # result = []
        # if len(nums1) > len(nums2):
        #     longer = nums1
        #     shorter = nums2
        # else:
        #     longer = nums2
        #     shorter = nums1
            
        # for num in shorter:
        #     if num in longer:
        #         result.append(num)
        # return list(set(result))

        
        # st = set(nums1)
        # result = []
        # for num in nums2:
        #     if num in st:
        #         result.append(num)
        #         st.remove(num)
        # return result