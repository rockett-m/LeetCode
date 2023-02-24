class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_dict = OrderedDict()
        
        uniq_set = set(s)
        uniq_list = []
        for idx, letter in enumerate(s):
            if letter not in my_dict.keys():
                my_dict[letter] = [idx, 1]
            else:
                count =  my_dict[letter][1] + 1
                my_dict.update({letter:[idx, count]})

        for k, v in my_dict.items():
            if v[1] == 1: # only 1 counts are good
                return v[0] # idx
        return -1 # no match