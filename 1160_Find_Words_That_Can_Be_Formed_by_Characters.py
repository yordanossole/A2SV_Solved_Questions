from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        char_counter = Counter(chars)
        for word in words:
            w_c = Counter(word)
            counter = 0
            for k, v in w_c.items():
                if not k in char_counter:
                    break
                if v <= char_counter[k]:
                    counter += v
            if counter == len(word):
                ans += len(word)
        return ans