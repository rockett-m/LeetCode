class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        my_dict = {}
        out = []
        for idx, val in enumerate(nums):
            if val not in my_dict.keys():
                my_dict[val] = 1
            else:
                my_dict[val] += 1
                out.append(val)
        return out