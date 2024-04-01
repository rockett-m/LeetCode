class Solution:
    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        self.index = len(self.nums)-1
        # store memoization where you can't rob negative money
        self.memo = OrderedDict((idx, max(0, val)) for idx, val in enumerate(self.nums))
        
        return self.recurse(self.index)

    
    def recurse(self, idx: int) -> int:
        if idx < 0:
            return 0
        elif idx == 0:
            return self.nums[0]
        
        for h in range(idx+1):
            if h == 0:
                self.memo[0] = self.nums[0]
            elif h == 1:
                self.memo[1] = max(self.nums[0], self.nums[1])
            else:
                # self.nums[h] cannot be less than 0 (set above)
                self.memo[h] = max(self.memo[h-1], self.nums[h] + self.memo[h-2])

        # print(f'{self.memo = }')
        return self.memo[idx]

