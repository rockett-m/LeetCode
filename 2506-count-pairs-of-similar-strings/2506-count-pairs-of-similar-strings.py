class Solution:
    def similarPairs(self, words: List[str]) -> int:
        output = []
        for w in words:
            w = ''.join(set(sorted(w)))
            output.append(w)
        print(output)
        # do counter and see if there are matching values
        counts = Counter(output)
        total = 0
        print(counts)
        for c,v in counts.items():
            if v > 1:
                # val of 2 means a and b are 1 pair
                # val of 3 means a,b and b,c and a,c give 3 pairs
                # val of 4 means a,b a,c a,d b,c b,d c,d give 6 pairs
                total += (v*(v-1)) // 2
        return total