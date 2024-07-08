class Solution:
    def myAtoi(self, s: str) -> int:
        # whitespace from left
        s = s.lstrip()
        if len(s) == 0: return 0
        # determine signedness
        neg = False
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-': neg = True
            # strip sign +/-
            if len(s) == 1: return 0
            s = s[1:]
        
        # longest int string is valid
        for i in range(len(s)):
            if not s[i].isdigit(): 
                s = s[:i]
                if len(s) == 0: return 0
                break

        # get int val and apply sign
        n = -int(s) if neg else int(s)
        # check signed int range
        if -2**31 <= n <= 2**31-1: return n
        # return rounded
        return -2**31 if neg else 2**31-1
            