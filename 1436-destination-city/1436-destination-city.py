class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dests = set([x[1] for x in paths])
        starts = [x[0] for x in paths]
        for d in dests:
            if d not in starts:
                return d
