class Solution:
    def rob(self, nums: List[int]) -> int:
        # store memoization where you can't rob negative money
        memo = OrderedDict((idx, max(0, val)) for idx, val in enumerate(nums))

        return self._memo_rob(memo, len(nums)-1)

    
    def _memo_rob(self, memo: OrderedDict, idx: int) -> int:
        if idx < 0:    return 0
        elif idx == 0: return memo[0]
            
        for h in range(1, idx+1):
            if h == 1:
                memo[h] = max(memo[h-1], memo[h])
                continue
            memo[h] = max(memo[h-1], memo[h] + memo[h-2])

        # print(f'{memo = }')
        return memo[idx]

