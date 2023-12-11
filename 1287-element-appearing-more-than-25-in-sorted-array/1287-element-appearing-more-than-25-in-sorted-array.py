class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # c = Counter(arr)
        # high = max(c.values())
        # return [k for k,v in c.items() if v == high][0]
        from statistics import mode
        return mode(arr)
    