from collections import defaultdict, OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_map =  {}
        self.freq_map = defaultdict(OrderedDict)
            

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        value, freq = self.key_map[key]
        del self.freq_map[freq][key]
        if not self.freq_map[freq] and freq == self.min_freq:
            self.min_freq += 1
        freq += 1
        self.freq_map[freq][key] = None
        self.key_map[key] = (value, freq)
        return value
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return 
        if key in self.key_map:
            self.key_map[key] = (value, self.key_map[key][1])
            self.get(key)
            return
        if self.size == self.capacity:
            evidct_key,_ = self.freq_map[self.min_freq].popitem(last = False)
            del self.key_map[evidct_key]
            self.size -= 1
        self.key_map[key] = (value, 1)
        self.freq_map[1][key] = None
        self.min_freq = 1
        self.size += 1

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)