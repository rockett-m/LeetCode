class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ''' passes 308 / 312 cases and runtime fail
        
        output = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):

                    trip = list([nums[i], nums[j], nums[k]])
                    if sum(trip) == 0: # save compute time
                        if sorted(trip) not in output:
                            output.append(sorted(trip))
        return output
        '''

        # ''' passes 308 / 312 cases and runtime fail
        output = []
        nums = sorted(nums)
        for i in range(len(nums)-2): # allows 2nd and 3rd digits to not overflow
            lp = i+1 # 1 greater than fixed idx
            rp = len(nums) - 1 # last
            while lp < rp:
                trip = list([nums[i], nums[lp], nums[rp]])
                
                if sum(trip) == 0:
                    if trip not in output:
                        output.append(trip)
                    lp += 1
                    rp -= 1
                # how do you decide which to increment/decrement?
                # see how the sum compares (nums are sorted remember)
                # can't edit both pointers at once or could skip combos
                elif sum(trip) < 0:
                    lp += 1
                else:
                    rp -= 1
                        
        return output
        # '''