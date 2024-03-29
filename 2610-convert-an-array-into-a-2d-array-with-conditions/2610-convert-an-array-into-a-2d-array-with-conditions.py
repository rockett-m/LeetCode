class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        c = Counter(sorted(nums))
        out = []

        while True:
            curr = []
            for k,v in c.items():
                if k not in curr and v > 0:
                    curr.append(k)
                    c[k] -= 1
            if len(curr) == 0:
                break
            out.append(curr)

        return out