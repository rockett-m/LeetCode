class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None]*n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey-1] = value

        # can't return beyond pointer's location, return blank if no val at ptr
        if idKey-1 > self.ptr or self.stream[self.ptr] is None:
            return []

        # can return from ptr to streak of values
        end = self.ptr
        for i in range(self.ptr, len(self.stream)):
            if self.stream[i] is not None:
                end += 1
            else:
                break

        start = self.ptr
        self.ptr = end

        return self.stream[start:end]

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)