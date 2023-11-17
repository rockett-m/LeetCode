class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a, b = s[0:len(s)//2], s[len(s)//2:]
        
        acount, bcount = 0, 0
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        for ai, bi in zip(a, b):
            if ai in vowels: acount += 1
            if bi in vowels: bcount += 1
        
        # print(acount, bcount)
        if acount == bcount: return True
        return False