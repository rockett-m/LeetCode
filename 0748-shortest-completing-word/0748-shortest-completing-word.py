class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lets = licensePlate.strip(' ').lower()
        let = []
        for i in lets:
            if i.isalpha():
                let.append(i)
        print(let)
        
        req = Counter(let)
        
        # loop through
        # use Counter on word to scan - to solve repeat letters
        # count >= required letter amount
        
        minn = -1
        out = []
        for w in words:
            bad = False
            wc = Counter(w)
            for kreq, vreq in req.items():
                if kreq in wc.keys():
                    if vreq > wc[kreq]:
                        bad = True
                        break
                else:
                    bad = True # bad etc
                    break

            if not bad:        
                if minn < 0 or len(w) < minn:
                    minn = len(w)
                    out = [w]
        
        good = ''
        for i in range(len(out)):
            if len(out[i]) <= minn:
                good = out[i]
                break
        
        return good