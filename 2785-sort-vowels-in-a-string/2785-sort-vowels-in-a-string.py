class Solution:
    def sortVowels(self, s: str) -> str:
        new = ''
        vows = []
        # store vowels as ord values and then sort and insert sorted vowels into final string
        for idx, val in enumerate(s):
            if ord(val) in [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]:
                vows.append(ord(val))
        
        srt = sorted(vows)
        curr = 0
        for idx, val in enumerate(s):
            if ord(val) not in [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]:
                new += val
            else:
                new += chr(srt[curr])
                curr += 1
        
        return new
                