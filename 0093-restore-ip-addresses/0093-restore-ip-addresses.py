class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        digits = set()
        if len(s) < 4 or len(s) > 12: return []
        if len(s) == 4: return ['.'.join(s)]
        
        def valid_chunk(chunk: str) -> bool:
            if not chunk: return False
            if len(chunk) > 1 and chunk[0] == '0': return False
            return 0 <= int(chunk) <= 255
        
        def backtrack(curr: str, rem: str, dots_count: int):
            
            if dots_count > 3: return
            
            if dots_count == 3 and valid_chunk(rem):
                digits.add(curr + rem)
                return

            # look at blocks of 1-3 digits
            for i in range(min(3, len(rem))):
                nxt = rem[:i+1]
                
                if valid_chunk(nxt):
                    backtrack(curr + nxt + '.', rem[i+1:], dots_count+1)

        backtrack('', s, 0)
        
        return list(digits)
