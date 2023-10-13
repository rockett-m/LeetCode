class Solution:
    def greatestLetter(self, s: str) -> str:
        both = []
        lowers = set()
        uppers = set()
        my_dict = OrderedDict()
        for i in s:
            if i.lower() == i:
                lowers.add(i)
            else:
                uppers.add(i)
        
        maxx = 0
        for x in lowers:
            if x.upper() in uppers:
                if ord(x.upper()) > maxx:
                    maxx = ord(x.upper())
        if maxx == 0: return ''
        return chr(maxx)