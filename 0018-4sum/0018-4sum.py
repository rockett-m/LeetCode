class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        out = set()

        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                a = nums[i]
                b = nums[j]

                lp, rp = j+1, len(nums)-1

                while lp < rp:

                    c = nums[lp]
                    d = nums[rp]
                    temp = (a, b, c, d)

                    if sum(temp) == target:
                        out.add(temp)
                        lp += 1
                    elif sum(temp) > target:
                        rp -= 1
                    else:
                        lp += 1

        return list(out)