class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xx = str(bin(x).split('b')[1])
        yy = str(bin(y).split('b')[1])

        if len(xx) > len(yy):
            yy = '0' * (len(xx) - len(yy)) + yy
        elif len(yy) > len(xx):
            xx = '0' * (len(yy) - len(xx)) + xx

        count = 0
        for i, j in zip(xx, yy):
            if i != j: count += 1
        return count