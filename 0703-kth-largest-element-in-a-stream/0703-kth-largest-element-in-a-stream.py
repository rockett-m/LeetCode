class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            _ = heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        # build heap if too small
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        # only update if kth score is smaller than val
        elif val > self.nums[0]:
            heapq.heappop(self.nums)
            heapq.heappush(self.nums, val)

        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)