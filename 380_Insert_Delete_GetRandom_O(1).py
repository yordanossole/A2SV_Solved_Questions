# leetcode
import random
class RandomizedSet:

    def __init__(self):
        self.my_list = []
        self.item_pos = {}
        

    def insert(self, val: int) -> bool:
        if val in self.item_pos:
            return False

        self.item_pos[val] = len(self.my_list)
        self.my_list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.item_pos:
            return False
        
        val_index = self.item_pos[val]
        last_item = self.my_list[-1]

        # this updates the position of the last item in my_list with the index of the value to deleted -> on item_pos
        self.item_pos[last_item] = val_index 
        self.my_list[val_index] = last_item # this overites the val

        self.my_list.pop() # remove the duplicated last item
        del self.item_pos[val] # remove val

        return True
        

    def getRandom(self) -> int:
        return random.choice(self.my_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()