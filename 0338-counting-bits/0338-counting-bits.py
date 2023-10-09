class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for i in range(n+1):
            x = str(str(bin(i)).split('b')[1])
            y = Counter(x)
            out.append(y['1'])
        return out