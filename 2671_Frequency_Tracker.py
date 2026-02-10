# leetcode
from collections import defaultdict
class FrequencyTracker:
    def __init__(self):
        self.num_freq = defaultdict(int)
        self.freq_counter = defaultdict(int)   

    def add(self, number: int) -> None:
        old_freq = self.num_freq[number]
        if old_freq > 0:
            self.freq_counter[old_freq] -= 1
        
        self.num_freq[number] += 1
        self.freq_counter[old_freq + 1] += 1

    def deleteOne(self, number: int) -> None:
        old_freq = self.num_freq[number]
        if old_freq == 0:
            return
        
        self.freq_counter[old_freq] -= 1 # remove from the old group
        self.num_freq[number] -= 1

        if self.num_freq[number] == 0:
            # no need to add into new group
            del self.num_freq[number]
        else:
            self.freq_counter[old_freq - 1] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_counter[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
