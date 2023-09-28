class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s_words = list(s.split(' '))
        if len(pattern) != len(s_words):
            return False

        num, numm = 0, 0
        comp = []; compa = []
        my_dict = OrderedDict()
        my_s_dict = OrderedDict()
        
        for let, lett in zip(pattern, s_words):
            if let not in my_dict.keys():
                my_dict[let] = num
                comp.append(num)
                num += 1
            else:
                comp.append(my_dict[let])
                
            if lett not in my_s_dict.keys():
                my_s_dict[lett] = numm
                compa.append(numm)
                numm += 1
            else:
                compa.append(my_s_dict[lett])
        
        return True if comp == compa else False
