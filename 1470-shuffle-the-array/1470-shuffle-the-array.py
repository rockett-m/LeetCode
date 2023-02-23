class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newList = []
        for i in range(n):
            newList.extend((nums[i], nums[i+n]))
            # newList.append(nums[i])
            # newList.append(nums[i+n])
            
        return newList