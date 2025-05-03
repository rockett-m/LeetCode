class Solution:
    def divisorGame(self, n: int) -> bool:
        turns = 0
        while n > 1:
            x = 1

            if n % x == 0:
                turns += 1
                n -= x
            else:
                break

        return True if turns % 2 == 1 else False