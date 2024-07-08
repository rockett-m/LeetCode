class Solution:
    def reverse(self, x: int) -> int:
        # stringify
        x = str(x)
        # check neg
        neg = True if x[0] == '-' else False
        # remove neg if there
        if neg: x = x[1:]
        # reverse str
        x = x[::-1]
        # apply neg back
        x = -int(x) if neg else int(x)
        # check valid range
        if -2**31 <= x <= 2**31-1: return x

        return 0
