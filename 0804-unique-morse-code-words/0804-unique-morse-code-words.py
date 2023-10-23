class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mcode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
            "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
            "..-","...-",".--","-..-","-.--","--.."]
        
        xforms = []
        
        for w in words:
            xform = []
            for idx, val in enumerate(w):
                x = ord(val) - 97
                print(x)
                xform.append(mcode[x])
            xforms.append(''.join(xform))
        return len(list(set(xforms)))