class Solution:
    def reformat(self, s: str) -> str:
        new_s = []

        num_count = sum([char.isdigit() for char in s])
        let_count = len(s) - num_count
        
        if (len(s) < 1) or (abs(num_count - let_count) > 1):
            return ''
        elif len(s) == 1:
            return s

        nums = []; lets = []
        
        for i in range(len(s)):
            if s[i].isdigit():
                nums.append(s[i])
            else:
                lets.append(s[i])

        for x in range(len(s)):

            if len(nums) == len(lets) and (len(new_s) == 0):
                new_s.append(lets[0])
                lets.pop(0)

            elif len(nums) == len(lets) and (len(new_s) > 0):
                if new_s[x-1].isdigit():
                    new_s.append(lets[0])
                    lets.pop(0)   
                else:
                    new_s.append(nums[0])
                    nums.pop(0)           

            elif len(nums) > len(lets):
                new_s.append(nums[0])
                nums.pop(0)
            elif len(lets) > len(nums):
                new_s.append(lets[0])
                lets.pop(0)

        return ''.join(new_s)
        
        
