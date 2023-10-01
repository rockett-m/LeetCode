class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alts = [0]
        for idx, curr in enumerate(gain):
            ele = alts[-1] + curr
            alts.append(ele)
        return max(alts)
                        