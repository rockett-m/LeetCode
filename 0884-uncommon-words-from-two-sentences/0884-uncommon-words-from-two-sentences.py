class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        cs1 = Counter(s1.split(' '))
        cs2 = Counter(s2.split(' '))

        uniq1 = [k for k,v in cs1.items() if v == 1]
        uniq2 = [k for k,v in cs2.items() if v == 1]

        return [x for x in uniq1 if x not in cs2.keys()] + \
                [x for x in uniq2 if x not in cs1.keys()]

        return out