# hackerrank
class Solution:
    def isSorted(self, arr) -> bool:
        if len(arr) < 2:
            return True

        left = 0
        right = 1        
        while right < len(arr):
            if arr[left] > arr[right]:
                return False
            left += 1
            right += 1

        return True