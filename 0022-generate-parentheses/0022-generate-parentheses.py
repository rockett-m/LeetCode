class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        
        def backtrack(s: str, l: 0, r: 0):
            
            if l == r == n:
                out.append(s)
                return

            if l < n:
                backtrack(f'{s}(', l+1, r)

            if r < l:
                backtrack(f'{s})', l,   r+1)

        backtrack('', 0, 0)

        return out