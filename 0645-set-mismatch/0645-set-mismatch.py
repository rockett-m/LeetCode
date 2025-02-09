class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup_miss = [0, 0]
        nums.sort()

        # # ensure 1 exists [at front]
        if nums[0] != 1:
            dup_miss[1] = 1
            # fix nums so it doesn't double count
            nums[0] == 1

        # we can modify the list in a while loop not a for loop
        i = 1
        while i < len(nums):
            # print(f'{i = }, {nums[i-1] = }, {nums[i] = }, {nums = }, {dup_miss = }')
            # duplicate found (+1 to 2nd num)
            if nums[i-1] == nums[i]:
                dup_miss[0] = nums[i-1]
                if 0 not in dup_miss:
                    return dup_miss

            # gap found
            if nums[i-1] + 2 == nums[i]:
                dup_miss[1] = nums[i-1] + 1
                if 0 not in dup_miss:
                    return dup_miss
            i += 1

        # the last number might be n-1 if we haven't seen a skip
        # but it should go to n, so this case adds n in
        if dup_miss[1] == 0:
            dup_miss[1] = nums[-1] + 1
    
        return dup_miss

