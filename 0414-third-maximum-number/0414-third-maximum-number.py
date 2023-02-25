from collections import Counter
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            return max(nums)

        high_to_low = sorted(list(set(nums)), reverse=True)
        if len(high_to_low) >= 3:
            return high_to_low[2]
        else:
            return high_to_low[0]
        
        
#         counts = Counter(nums)
#         print(counts)
#         print([i for i in counts if counts[i] == 1])
#         uniq = [i for i in counts if counts[i] == 1]
#         if len(uniq) >= 3:
#                     return sorted(list(set(nums)), reverse=True)[2]

#             # return uniq[2]
#             return sorted(counts, key=counts.get, reverse=True)[2]
#         else:
#             # return uniq[0]
#             # sorted(counts, key=counts.get, reverse=True)[2]
#             # counts.sorted()[0]
#             return counts[0]
