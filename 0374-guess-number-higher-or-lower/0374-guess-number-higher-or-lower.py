# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        num = 1
        self.done = False
        lower, upper = 1, n
        
        code = guess(n)
        if code == 0:
            return n

        while not self.done:
            
            midpoint = 0
            if lower % 2 == 0 and upper % 2 == 0:
                midpoint = (lower + upper+1) // 2
            else:
                midpoint = (lower + upper) // 2

            code = guess(midpoint)
            print(midpoint, code, lower, upper)

            if code == -1: # my guess is higher
                upper = midpoint
            elif code == 1: # my guess is lower
                lower = midpoint
            elif code == 0: # done, correct
                return midpoint

        return num
            
            
#             code = self.check(num) # looking to set too_high flag
#             if code == 0:
#                 return num

#             midpoint = (num + n) // 2
#             code = self.check(midpoint)
#             if code == -1:
#                 num = midpoint
#             elif code == 1:
                
                
                
#             if not self.too_high: # increase num when not too high
#                 # num = num ** 2
#                 # num = num + num // 2
#                 self.check(midpoint)

#             elif self.too_high: # subtract 1 until num found (too slow)
#                 num -= 1
#                 # self.check(num)
#                 self.check(midpoint)

#         return num


#     def check(self, num): # if too high, then subtract until equal (match found)

#         code = guess(num) # get the -1, 0, 1 indicator
        
#         if code == 0: # done
#             self.done = True

#         elif code == -1: # set key flag to trigger subtraction until goal
#             self.too_high = True

#         return code