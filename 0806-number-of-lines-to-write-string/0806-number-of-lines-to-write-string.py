class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        result = [1, 0]
        # result[0] is the total number of lines.
        # result[1] is the width of the last line in pixels.
        # total = sum(widths)
        curr = 0
        
        for idx, w in enumerate(s):
            trans = widths[ord(w) - 97]
            if curr + trans <= 100:
                curr += trans
            else:
                result[0] += 1 # one line longer
                curr = trans
            # total -= w
        result[1] = curr
        return result