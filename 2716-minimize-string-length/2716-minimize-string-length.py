class Solution:
    def minimizedStringLength(self, s: str) -> int:
        
        # if len(set(s)) == len(s):
        return len(set(s))

#         out = s[0]
#         for idx, val in enumerate(s):
#             l = idx-1
#             r = idx+1
#             if idx > 0 and idx+1 < len(s):

#                 if s[l] != val:
#                     out += val
                    
#             if idx == len(s) - 1 and val != s[l]:
#                  out += val

                    
#         print(out)
#         return len(out)