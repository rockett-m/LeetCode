class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = []
    
        while not self.finish_check(columnNumber):
            # build right to left, reverse at end
            columnNumber -= 1
            letters.insert(0, chr((columnNumber % 26) + 65))
            columnNumber //= 26

        # final conversion
        if columnNumber % 26 == 0:
            letters.insert(0, chr(26 + 64))
        else:
            letters.insert(0, chr((columnNumber % 26) + 64))

        return "".join(letters)

    def finish_check(self, num) -> bool:
        """ return True if final letter """
        if num < 27:
            return True
        return False
