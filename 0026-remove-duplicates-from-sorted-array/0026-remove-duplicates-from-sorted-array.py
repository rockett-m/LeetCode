class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(list(set(nums)))
        print(nums)
        return len(nums)
#         prev = ''
#         # for i in range(len(nums)):
#         i = 0
#         while i < len(nums):
#             curr = nums[i]
#             print(f'S {i = }, {prev = }, {curr = }')
            
#             if prev == '': # first elem
#                 prev = curr
#                 i += 1

#             elif curr == '_':
#                 print(f'break: {prev = } : {curr = } {nums = }')
#                 break

#             elif prev != nums[i]: # prev != curr
#                 prev = curr
#                 i += 1

#             elif prev == curr:
#                 print(f'else B: {prev = } : {curr = } {nums = }')
#                 nums.append('_')
#                 nums.pop(i)
#                 print(f'else A: {prev = } : {curr = } {nums = }')
#                 # since we reduce list indexing we need to loop accordingly

#             print(f'E {i = }, {prev = }, {curr = }')

#         print(nums, sum([str(char).isnumeric() for char in nums]))
#         return sum([str(char).isnumeric() for char in nums])