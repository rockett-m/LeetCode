class Solution:
    def digitCount(self, num: str) -> bool:
        count = 0
        c = Counter(num)
        for idx, val in enumerate(num):
            if str(idx) not in c.keys() and int(val) != 0 or (int(val) != c[str(idx)]):
                return False

        return True