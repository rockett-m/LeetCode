class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max = 0
        for s in strs:
            l = ''
            if re.search(r'[a-z]', s):
                l = len(s)
            else:
                l = int(s)
            if l > max: max = l
        return max