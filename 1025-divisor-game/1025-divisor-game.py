class Solution:
    def divisorGame(self, n: int) -> bool:
        turns = 0

        while n > 1:
            turns += 1
            n -= 1

        return True if turns % 2 == 1 else False