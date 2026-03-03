# leetcode
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0] * (n+1)      
        
        for l,r,d in shifts:
            if d == 0:
                prefix[l] -= 1
                prefix[r+1] += 1
            else:
                prefix[l] += 1
                prefix[r+1] -= 1

        run_sum = 0
        result = []
        for i, char in enumerate(s):
            run_sum += prefix[i]
            val = ord(char) - ord("a")
            new_val = (run_sum + val) % 26
            result.append(chr(new_val + ord("a")))
        return "".join(result)