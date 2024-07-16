class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        ans = ''
        
        letters = []
        for k,v in c.items():
            if v > 0:
                letters.append((-v, k))
        
        heapify(letters)
        
        def push_back(letters, occ, let):
            if abs(occ) > 0:
                heappush(letters, (occ, let))
                
        while letters:
            if not ans:
                occ, let = heappop(letters)
                ans += let
                occ += 1
                push_back(letters, occ, let)

            elif ans:
                occ, let = heappop(letters)
                
                if let != ans[-1]:
                    ans += let
                    occ += 1
                    push_back(letters, occ, let)
                else:
                    if not letters: 
                        ans = ''
                        break
                    occ2, let2 = heappop(letters)
                    ans += let2
                    occ2 += 1
                    push_back(letters, occ, let)
                    push_back(letters, occ2, let2)
            else:
                ans = ''
                break
                
        return ans