class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        transform = sorted(score, reverse=True)
        my_dict = {}
        for idx, val in enumerate(transform):
            if idx == 0:
                my_dict[val] = "Gold Medal"
            elif idx == 1:
                my_dict[val] = "Silver Medal"
            elif idx == 2:
                my_dict[val] = "Bronze Medal"
            else:
                my_dict[val] = str(idx+1)
        
        out = []
        for i in score:
            out.append(my_dict[i])
    
        return out