class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        from sortedcontainers import SortedList
        self.nums = SortedList(nums)
        self.k = k

    def add(self, val: int) -> int:
        # insert number into sorted list preserving order
        self.nums.add(val)
        return self.nums[-self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)