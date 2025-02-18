class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        b = bin(n).lstrip('0b')[::-1]
        out = [0,0]
        for i in range(len(b)):
            if int(b[i]) == 1:
                if i % 2 == 0:
                    out[0] += 1
                else:
                    out[1] += 1
        return out