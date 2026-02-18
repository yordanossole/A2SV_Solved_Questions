# leetcode
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Counting sort (heights are unique)
        max_height = max(heights)
        count = [""] * (max_height+1)

        for i in range(len(heights)):
            count[heights[i]] = names[i]
        
        result = []
        for i in range(len(count)-1, -1, -1):
            if count[i] != "":
                result.append(count[i])
        
        return result

        # # Insertion sort - key based (classic)
        # for i in range(1, len(names)):
        #     name = names[i]
        #     height = heights[i]
            
        #     j = i - 1
        #     while j >=0 and height > heights[j]:
        #         heights[j+1] = heights[j]
        #         names[j+1] = names[j]
        #         j -= 1

        #     heights[j+1] = height
        #     names[j+1] = name
        
        # return names      
        
        # # Insertion sort - swapping based
        # for i in range(1, len(names)):
        #     for j in range(i, 0, -1):
        #         if heights[j] > heights[j-1]:
        #             names[j], names[j-1] = names[j-1], names[j]
        #             heights[j], heights[j-1] = heights[j-1], heights[j]
        #         else:
        #             break
        # return names

        # # Selection sort
        # for i in range(len(names)):
        #     max_i = i
        #     for j in range(i+1, len(names)):
        #         if heights[j] > heights[max_i]:
        #             max_i = j

        #     names[i], names[max_i] = names[max_i], names[i]
        #     heights[i], heights[max_i] = heights[max_i], heights[i]
        # return names

        # # Bubble sort
        # for i in range(len(names)):
        #     swapped = False
        #     for j in range(len(names)-1-i):
        #         if heights[j] < heights[j+1]:
        #             names[j], names[j+1] = names[j+1], names[j]
        #             heights[j], heights[j+1] = heights[j+1], heights[j]
        #             swapped = True
        #     if not swapped:
        #         break
        # return names