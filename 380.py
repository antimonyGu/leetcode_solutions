class RandomizedSet:
    def __init__(self):
        self.data_map = {} # val to index
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        
        self.data_map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if not val in self.data_map:
            return False
        
        last_elem = self.data[-1]
        index_of_elem_to_remove = self.data_map[val]
        # last elem's index should be index of elem to remove
        self.data_map[last_elem] = index_of_elem_to_remove

        # swap val with last elem
        self.data[index_of_elem_to_remove] = last_elem
        self.data[-1] = val
        # pop val
        self.data.pop()
        self.data_map.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()