class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        my_dict = {}
        for idx, match in enumerate(matches):

            winner = str(match[0])
            loser = str(match[1])
            
            if winner not in my_dict.keys():
                my_dict[winner] = [1,0]
            elif winner in my_dict.keys():
                val = my_dict[winner]
                val[0] += 1
                my_dict.update({winner:val})        
                
            if loser not in my_dict.keys():
                my_dict[loser] = [0,1]
            
            elif loser in my_dict.keys():
                val = my_dict[loser]
                val[1] += 1
                my_dict.update({loser:val})
        
        
        out = []
        zero = []
        one = []
        
        for k,v in my_dict.items():
            if v[1] == 1:
                one.append(int(k))
            elif v[1] == 0:
                zero.append(int(k))

        zero.sort()
        one.sort()
        return [zero] + [one]
        # out.append(zero)
        # out.append(one)
        # return out
        