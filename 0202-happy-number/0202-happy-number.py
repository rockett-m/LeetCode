class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        while n > 1:
            new = []
            nn = str(n)
            for i in range(len(nn)):
                new.append(int(nn[i]) ** 2)

            total = 0
            for x in new:
                total += x
            if total == 1:
                return True
            if total < 10 and total % 2 == 0:
                return False
            n = total

        return False