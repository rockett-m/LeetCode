class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        best = 0
        sfn_list = sorted(satisfaction)
        
        while len(sfn_list) > 0:
            total = 0
            added_idx = 0
            for idx, score in enumerate(sfn_list):
                # print(idx, score)
                # if score > 0:
                added_idx += 1

                total += added_idx * score

            if total > best:
                best = total
            sfn_list.pop(0)

        print(best)
            
            
        if best <= 0:
            return 0

        return best