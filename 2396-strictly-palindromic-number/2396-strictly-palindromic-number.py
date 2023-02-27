class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        conv = list(str(bin(n)[2:]))
        mid = floor(len(conv)//2)
        if (len(conv) % 2 == 0) and (conv[0:mid] is conv[mid+1:].reverse()): # even
            return True
        elif conv[0:mid] is conv[mid:].reverse(): # share mid
            return True
        return False