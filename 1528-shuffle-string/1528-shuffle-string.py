class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        comb = []
        for str, ind in zip(s, indices):
            comb.append([str, ind])
            
        return ''.join([x[0] for x in sorted(comb, key=lambda comb: comb[1])])
            