class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total = 0
        for typ in ['M', 'P', 'G']:
            travel_time = 0
            found = False
            for idx, val in enumerate(reversed(garbage)):
                c = Counter(val)
                if typ in c.keys():
                    total += c[typ] # house_time
                    if not found:
                        final_house = len(garbage) - 1 - idx
                        found = True

            if found:
                travel_time = sum([z for z in travel[0:final_house]])
                total += travel_time
            
        return total