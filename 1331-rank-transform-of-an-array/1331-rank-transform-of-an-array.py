class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        srt = list(set(arr))
        srt.sort()
        my_d = {}
        for idx, val in enumerate(srt):
            my_d[val] = idx + 1

        return [my_d[val] for idx, val in enumerate(arr)]
