class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        my_dict = OrderedDict()
        for n in nums:
            if n not in my_dict.keys():
                my_dict[n] = 1
            else:
                my_dict[n] += 1

        k = 0
        for key, val in my_dict.items():
            # print(f'{key = } {val = }')
            for i in range(min(val, 2)):
                nums[k] = key
                k += 1
                # print(f'{nums = } {k = }')

        return k