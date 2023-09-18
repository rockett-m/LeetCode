class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
        if s1 == s2: return True

        test = list(s1)
        for i, let in enumerate(s1):
            j = i+2
            if j < len(s1):
                if test[i] != s2[i] or test[j] != s2[j]:
                    test[i] = s1[j]
                    test[j] = s1[i]
                    if ''.join(test) == s2:
                        return True
        return False