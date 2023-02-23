class Solution:
    def reduce_list(self, list_in: list, merge_list: list):
        merge_list.append(list_in[0])
        list_in.pop(0)

    def reformat(self, s: str) -> str:

        num_count = sum([char.isdigit() for char in s])
        let_count = len(s) - num_count
        
        if (len(s) < 1) or (abs(num_count - let_count) > 1):
            return ''

        nums = []; lets = []; new_s = []
        
        for i in range(len(s)):
            if s[i].isdigit():
                nums.append(s[i])
            else:
                lets.append(s[i])

        for x in range(len(s)):

            if len(nums) == len(lets):
                if len(new_s) == 0:
                    self.reduce_list(lets, new_s)
                elif new_s[x-1].isdigit(): # not zero, check prev type
                    self.reduce_list(lets, new_s)
                else:
                    self.reduce_list(nums, new_s)

            elif len(nums) > len(lets):
                self.reduce_list(nums, new_s)

            elif len(lets) > len(nums):
                self.reduce_list(lets, new_s)

        return ''.join(new_s)
