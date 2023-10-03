class Solution:
    def judgeCircle(self, moves: str) -> bool:
        vert = 0
        side = 0
        
        ans = Counter(moves)
        
        return True if ans['L'] - ans['R'] == 0 and ans['U'] - ans['D'] == 0 else False
        
#         for i in moves:
#             if i == 'U': vert += 1
#             elif i == 'D': vert -= 1
#             elif i == 'L': side -= 1
#             elif i == 'R': side += 1
        
#         return True if vert == 0 and side == 0 else False