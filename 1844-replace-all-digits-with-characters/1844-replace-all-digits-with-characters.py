class Solution:
    def replaceDigits(self, s: str) -> str:
        out = []
        for idx, val in enumerate(s):
            if idx % 2 != 0: # odd - number expected
                temp = s[idx-1] + str(chr(ord(s[idx-1])+int(val)))
                out.append(temp)
            if (idx == len(s) - 1) and (idx % 2 == 0): # even final just append
                out.append(val)
        return ''.join(out)
    