class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        output = []
        nums = sorted(nums)
        for i in range(len(nums)-2): # allows 2nd and 3rd digits to not overflow
            lp = i+1 # 1 greater than fixed idx
            rp = len(nums) - 1 # last
            while lp < rp:
                trip = list([nums[i], nums[lp], nums[rp]])
                
                # how do you decide which to increment/decrement?
                # see how the sum compares (nums are sorted remember)
                if sum(trip) == 0:
                    if trip not in output:
                        output.append(trip)
                    # change both pointers because we need unique triplets
                    lp += 1
                    rp -= 1

                elif sum(trip) < 0:
                    lp += 1
                else:
                    rp -= 1
                        
        return output
