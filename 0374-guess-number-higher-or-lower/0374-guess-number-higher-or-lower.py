# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        code = guess(n)
        if code == 0: return n # trivial

        lower, upper = 1, n
        
        while True:

            midpoint = 0
            if lower % 2 == 0 and upper % 2 == 0:
                upper += 1 # for floor division compatibility
            midpoint = (lower + upper) // 2

            code = guess(midpoint)

            if code == -1: # my guess is higher
                upper = midpoint
            elif code == 1: # my guess is lower
                lower = midpoint
            elif code == 0: # done, correct
                return midpoint