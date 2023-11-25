class Solution:
    def minOperations(self, boxes: str) -> List[int]:
#         out = [0]*len(boxes)
#         for idx, val in enumerate(boxes):
#             for ix, vl in enumerate(boxes):
#                 if idx != ix:
#                     out[idx] += abs(idx - ix)*int(vl)
            
#         return out
    
        out = [0]*len(boxes)
        for idx, val in enumerate(boxes):
            lp, rp = 0, len(boxes)-1
            while lp < idx:
                out[idx] += (idx-lp)*int(boxes[lp])
                lp += 1
            while rp > idx:
                out[idx] += (rp-idx)*int(boxes[rp])
                rp -= 1
        return out
