class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        conv = list(str(bin(n)[2:]))
        
        mid = floor(len(conv)//2)
        if len(conv) % 2 == 0: # even
            if conv[0:mid] is conv[mid+1:].reverse():
                return True
        else: # odd
            # if [ceil(len(conv)/2)):]
            if conv[0:mid] is conv[mid:].reverse():
                return True
        return False