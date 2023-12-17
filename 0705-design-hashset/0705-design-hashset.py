class MyHashSet:

    def __init__(self):
        self.hs = OrderedDict()

    def add(self, key: int) -> None:
        self.hs[key] = ''

    def remove(self, key: int) -> None:
        if key in self.hs.keys():
            del self.hs[key]

    def contains(self, key: int) -> bool:
        return True if key in self.hs.keys() else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)