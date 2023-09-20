class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        my_dict = dict()
        for w in words1:
            if w not in my_dict.keys():
                my_dict[w] = 1
            else:
                my_dict[w] = 1000

        for z in words2:
            if z in my_dict.keys():
                my_dict[z] += 1
        
        count = 0
        for k,v in my_dict.items():
            if v == 2: # 1 occurence in words1 - good
                count += 1
        return count