class Solution:
    def modifyString(self, s: str) -> str:

        lets = 'abcdefghijklmnopqrstuvwxyz'
        s = list(s)

        for idx, curr in enumerate(s):
            if curr == '?':
                for let in lets:
                    if idx == len(s) - 1:
                        if let != s[idx-1]:
                            s[idx] = let
                            return ''.join(s)
                    elif idx == 0:
                        if let != s[idx+1]:
                            s[idx] = let
                            break
                    elif idx != 0:
                        if let != s[idx-1] and let != s[idx+1]:
                            s[idx] = let
                            break
        return ''.join(s)
