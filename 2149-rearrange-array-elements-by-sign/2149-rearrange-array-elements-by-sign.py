class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        
        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        
        out = []
        print(pos, neg)
        pc, nc = 0, 0
        # for idx, val in enumerate(nums):
        for i in range(len(nums)):
            if i % 2 == 0:
                out.append(pos[pc])
                pc += 1
            else:
                out.append(neg[nc])
                nc += 1

        return out