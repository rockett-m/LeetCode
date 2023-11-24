class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)
        
        ptr = k
        maxx = sum(cardPoints[0:ptr]) + sum(cardPoints[len(cardPoints)-k+ptr:])
        ptr -= 1
        prevsum = maxx
        
        while ptr >= 0:
            lp = ptr
            rp = len(cardPoints)-k+ptr
            
            summ = prevsum - cardPoints[lp] + cardPoints[rp]
            
            if summ > maxx: maxx = summ
                
            ptr -= 1
            prevsum = summ
        
        return maxx
