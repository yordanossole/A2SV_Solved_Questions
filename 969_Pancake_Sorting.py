# leetcode
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []
        for i in range(n, 0, -1):
            pointer = arr.index(i)
            if pointer+1 != i:
                result.append(pointer+1)
                temp1 = arr[pointer::-1]
                temp2 = arr[pointer+1:]
                arr = [*temp1, *temp2]
                arr = arr[i-1::-1]
                result.append(i)
        return result