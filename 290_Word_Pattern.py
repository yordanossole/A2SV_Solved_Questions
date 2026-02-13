# leetcode
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False

        # dictionary to maintain both direction mapping
        both_map = {}

        for char, word in zip(pattern, words):
            p_key = ("char", char)
            w_key = ("word", word)

            if p_key in both_map and both_map[p_key] != word: # if it is already mapped to another word
                return False

            if w_key in both_map and both_map[w_key] != char: # if it is already mapped to another pattern char
                return False
            
            both_map[p_key] = word
            both_map[w_key] = char
        
        return True
