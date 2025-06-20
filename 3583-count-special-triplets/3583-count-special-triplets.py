class Solution:
    def specialTriplets(self, nums: List[int]) -> int:

        modulo = 10**9 + 7
        total = 0
        """
        nums[i] == nums[j] * 2
        nums[k] == nums[j] * 2
        """
        counts = Counter(nums)
        seen = {}
    
        for idx, val in enumerate(nums):
            target = val * 2

            counts[val] -= 1
            if counts[val] == 0: del counts[val]

            lcount = seen[target] if target in seen.keys() else 0
            rcount = counts[target] if target in seen.keys() else 0

            total += lcount * rcount
            total %= modulo

            if val in seen.keys():
                seen[val] += 1
            else:
                seen[val] = 1

        return total