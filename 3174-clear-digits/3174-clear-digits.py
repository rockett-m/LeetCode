class Solution:
    def clearDigits(self, s: str) -> str:

        while len(s) > 1:

            size_change = False
            for i in range(1, len(s)):
                # num and let
                if 48 <= ord(s[i]) <= 57 and \
                    97 <= ord(s[i-1].lower()) <= 122:
                    size_change = True
                    s = s[:i-1]+s[i+1:] if i<len(s)-1 else s[:i-1]
                    break

            if not size_change: return s
        return s