class Solution:
    def frequencySort(self, s: str) -> str:
        res = Counter(s)
        out = ''
        
        for k,v in res.most_common():
            
            out += k*v
        
        return out