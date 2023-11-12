class Solution:
    def countSubstrings(self, s: str) -> int:
        count = len(list(s))
        if len(s) > 1 and s == s[::-1]: count += 1
        if len(s) < 3: return count
        
        for i in range(2, len(s)):
            j = 0
            while j+i <= len(s):
                if s[j:j+i] == s[j:j+i][::-1]:
                    count += 1
                j += 1
        return count