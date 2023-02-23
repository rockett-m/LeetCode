class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        result = []

        for i in range(len(candies)):

            if ( (extraCandies + candies[i]) - max(candies) ) >= 0:
                result.append(True)
            else:
                result.append(False)

        return result