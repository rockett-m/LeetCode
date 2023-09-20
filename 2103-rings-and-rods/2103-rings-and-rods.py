class Solution:
    def countPoints(self, rings: str) -> int:
        my_dict = dict()
        count = 0
        for idx, val in enumerate(rings):
            if idx % 2 == 0: # color
                rod = rings[idx+1] # rod
                if rod not in my_dict.keys():
                    my_dict[rod] = set(val)
                else:
                    my_dict[rod].add(val)

        for k,v in my_dict.items():
            if len(v) == 3:
                count += 1
        return count
        