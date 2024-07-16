class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        banned = [ "aaa", "bbb", "ccc" ]
        ans = ''
        
        def push_back(letters, occ, let):
            if abs(occ) > 0:
                heappush(letters, (occ, let))
            
        letters = []
        for occ, let in zip([a, b, c], ['a', 'b', 'c']):
            if occ == 0: continue
            letters.append((-occ, let))

        heapq.heapify(letters)
        
        while letters:
            print(letters)
            occ, let = heappop(letters)
            
            occ *= -1
            tmp = ans + let

            if len(ans) >= 2 and ans[-2:] == let*2:
                if not letters: break

                occ2, let2 = heappop(letters)
                occ2 *= -1
                
                ans += let2
                occ2 -= 1
                
                push_back(letters, -occ2, let2)
                push_back(letters, -occ, let)

            else:
                amt = min(2, occ)
                
                ans += let*amt
                occ -= amt

                push_back(letters, -occ, let)
            # ans == '' then drain up to 2 of biggest let
            # len(ans) == 1: drain up to 2 of biggest let
            # len(ans) >= 2: drain up to 2 of biggest let
            
            print(occ, let, tmp, ans)

        
        return ans