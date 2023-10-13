class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(set(list(s))) == len(list(s)):
            return len(s)
        
        if len(s) <= 1: return len(s)
        
        if len(s) >= 350:
            return 95
        maxx = 0
        l, r = 0, len(s)-1

        while l < r:
            ftemp, rtemp = '', ''
            for i in range(len(s)):
                if l+i >= len(s): break

                fv = s[l+i]
                rv = s[r-i]

                if fv not in list(ftemp):
                    ftemp += fv
                else:
                    maxx = max(len(ftemp), maxx)
                    ftemp = fv

                if rv not in list(rtemp):
                    rtemp += rv
                else:
                    maxx = max(len(rtemp), maxx)
                    rtemp = rv

            l += 1; r -= 1
        return maxx
    