class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.elements = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.elements.keys():
            self.elements.move_to_end(key)
            return self.elements[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # print(f'{self.elements = }')
        if key not in self.elements.keys() and len(self.elements.keys()) + 1 > self.capacity: # evict
            self.elements.popitem(last=False)
        elif key in self.elements.keys():
            self.elements.move_to_end(key)
        self.elements[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)