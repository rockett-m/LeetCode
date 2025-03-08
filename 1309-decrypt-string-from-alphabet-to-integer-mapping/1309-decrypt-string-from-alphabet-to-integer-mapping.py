class Solution:
    def freqAlphabets(self, s: str) -> str:
        rp = len(s) - 1
        out = []
        while rp >= 0:
            # 10-26
            if s[rp] == '#': # the 2 digits to the left
                out += chr(int(s[rp-2:rp])+96)
                rp -= 2

            else:
                out += chr(int(s[rp])+96)
            rp -= 1

        return ''.join(out[::-1])