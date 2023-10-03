class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 3:
            tot = 1
            for i in nums:
                tot *= i
            return tot
        
        pos_max = sorted(nums)[-3:]
        neg_max = sorted(nums)[0:2]
        neg_max.append(max(nums))

        pmax, nmax = 1, 1
        for i,j in zip(pos_max, neg_max):
            pmax *= i
            nmax *= j
            
        return pmax if pmax > nmax else nmax