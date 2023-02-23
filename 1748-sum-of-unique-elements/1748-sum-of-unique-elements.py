class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        my_dict = {}
        for i in sorted(nums):
            if i not in my_dict.keys():
                my_dict[i] = 1
            else:
                my_dict[i] += 1
        
        uniques = []
        for k,v in my_dict.items():
            if v == 1:
                uniques.append(k)

        return sum(uniques)