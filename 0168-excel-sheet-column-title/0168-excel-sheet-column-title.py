class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = []
    
        while not self.finish_check(columnNumber):
            # build right to left, reverse at end
            columnNumber -= 1
            letters.insert(0, chr((columnNumber % 26) + 65))
            columnNumber //= 26

        # final conversion
        ans = ""
        if columnNumber % 26 == 0:
            ans = chr(26 + 64)
        else:
            ans = chr((columnNumber % 26) + 64)
        letters.insert(0, ans)

        return "".join(letters)

    def finish_check(self, num) -> bool:
        """ return True if final letter """
        if num < 27:
            return True
        return False


