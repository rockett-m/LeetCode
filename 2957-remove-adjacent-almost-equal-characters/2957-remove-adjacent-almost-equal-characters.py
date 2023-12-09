class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        if len(word) == 1: return 0
        
        ops = 0
        prev = False
        lp, rp = 0, 1

        while rp < len(word):
            l, r = word[lp], word[rp]
            
            if prev:
                prev = False

            elif abs(ord(l) - ord(r)) <= 1:
                ops += 1
                prev = True
            
            lp += 1; rp += 1
            
        return ops