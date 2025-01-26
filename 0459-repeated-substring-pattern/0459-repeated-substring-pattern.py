class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(set(s)) == 1 and len(s) > 1: return True
        leng = len(s)
        # must repeat 1+ times, so substring can't be larger than half of s
        for i in range(1, len(s)//2 + 1):
            # substring needs to go in cleanly for it to work
            if leng % i == 0:
                if ''.join(s[0:i]) * (leng // i) == s:
                    return True

        return False