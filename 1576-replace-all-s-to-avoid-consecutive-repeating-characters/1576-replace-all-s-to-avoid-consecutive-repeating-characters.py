class Solution:
    def modifyString(self, s: str) -> str:

        lets = 'abcdefghijklmnopqrstuvwxyz'
        s = list(s)

        for idx, curr in enumerate(s):
            if idx == len(s) - 1:
                if curr == '?':
                    for let in lets:
                        if let != s[idx-1]:
                            s[idx] = let
                            break
                return ''.join(s)
            
            elif curr == '?':
                # insert letter that doesn't match prev or curr
                for let in lets:
                    if idx != 0:
                        if let != s[idx-1] and let != s[idx+1]:
                            s[idx] = let
                            break
                    else:
                        if let != s[idx+1]:
                            s[idx] = let
                            break
   
