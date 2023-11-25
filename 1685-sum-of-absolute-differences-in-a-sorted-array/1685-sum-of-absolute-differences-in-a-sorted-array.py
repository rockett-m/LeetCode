class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        result = []
        prev = 0
        below, above = 0, sum(nums)
        for idx, val in enumerate(nums):
            above -= val
            if prev == val:
                result.append(result[idx-1])
            else:
                # result.append( val*idx - sum(nums[0:idx]) + sum(nums[idx+1:]) - val*(len(nums)-1-idx) )
                result.append( val*idx - below + above - val*(len(nums)-1-idx) )
            below += val
            prev = val
        return result
