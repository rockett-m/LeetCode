class Solution:
    def maxArea(self, height: List[int]) -> int:
    
        start = 0
        end = len(height)-1
        max_area = 0

        while start < end:
            
            area = (end-start) * min(height[start], height[end])
            if area > max_area: max_area = area

            if height[start] > height[end]: # try to seek higher height at end
                end -= 1
            else:
                start += 1
            
        return max_area

#         max_area = 0
#         for count, ht in enumerate(height):
            
#             for idx, avail_h in enumerate(height[count+1:]):
                
#                 area = min(ht, avail_h) * (idx+count+1 - count) # h * w
#                 if area > max_area: max_area = area

#         return max_area