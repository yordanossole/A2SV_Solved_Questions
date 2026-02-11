# leetcode
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while True:
            temp = 0
            while True:
                if n == 0:
                    n = temp
                    break
                last_d = n%10
                temp += last_d ** 2
                n //= 10

            if temp in visited:
                return False
            if temp == 1:
                return True
            visited.add(temp)
        
        return False
