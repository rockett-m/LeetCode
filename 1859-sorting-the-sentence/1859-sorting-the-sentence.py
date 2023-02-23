class Solution:
    def sortSentence(self, s: str) -> str:
    
        sent = s.split(' ')
        comb = []
        
        for i in range(len(sent)):

            res = [int(sent[i][-1]), sent[i][0:-1]]
            comb.append(res)
        
        out = [ k[1] for k in sorted(comb) ]

        return ' '.join(out)
