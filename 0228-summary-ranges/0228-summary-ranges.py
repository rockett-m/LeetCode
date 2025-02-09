class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        if len(nums) == 1: return [f"{nums[0]}"]

        ranges = [f"{nums[0]}"]
        # start streak (can't lookback to i-1 element here)
        if nums[0] + 1 == nums[1]:
            ranges[-1] += "->"

        for i in range(1, len(nums)):
            # last element
            if i == len(nums) - 1:
                # close streak
                if nums[i-1] + 1 == nums[i]:
                    ranges[-1] += f"{nums[i]}"
                # solo num
                else:
                    ranges.append(f"{nums[i]}")
                break

            # existing streak (end or do nothing)
            if nums[i-1] + 1 == nums[i]:
                # streak ends here
                if nums[i] + 1 != nums[i+1]:
                    ranges[-1] += f"{nums[i]}"

            # begin future streak
            elif nums[i] + 1 == nums[i+1]:
                ranges.append(f"{nums[i]}->")

            # island num
            else:
                ranges.append(f"{nums[i]}")

            # print(f'{ranges = }')

        return ranges