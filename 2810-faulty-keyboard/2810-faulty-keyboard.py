class Solution:
    def finalString(self, s: str) -> str:
        out = ''
        for i in range(len(s)):
            if s[i] == "i":
                out = out[::-1]
            else:
                out += s[i]
        return out