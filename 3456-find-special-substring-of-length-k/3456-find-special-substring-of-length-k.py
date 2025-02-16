class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        if len(s) == 1: return True
            
        let = s[0]
        streak = 1
        for i in range(1, len(s)):
            # first char
            if k == 1 and i == 1 and s[i] != let:
                return True

            # typical cases
            if s[i] == let:
                streak += 1
            elif s[i] != let:
                streak = 1
                let = s[i]

            # potentially done
            if streak == k and (i == len(s) - 1 or s[i+1] != s[i]):
                return True
                    
        return False