class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        out = []
        start, end = 0, 0
        num = ''
        for idx, w in enumerate(word):
            if not w.isdigit():
                if num != '':
                    out.append(num)
                num = ''; start, end = 0, 0
            else:
                if start == 0:
                    start = idx
                    num = w
                end = idx
                if end > start:
                    num += w
                if idx == len(word)-1:
                    out.append(num)

        out = [int(x) for x in out]
        return len(set(out))