class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        out = []
        for word in words:
            my_dict = {'qwertyuiop':0, 'asdfghjkl':0, 'zxcvbnm':0}
            test = word.lower()
            print(test)
            for let in range(len(test)):
                print(let)
                if test[let] in list('qwertyuiop'):
                    my_dict['qwertyuiop'] += 1
                elif test[let] in list('asdfghjkl'):
                    my_dict['asdfghjkl'] += 1
                elif test[let] in list('zxcvbnm'):
                    my_dict['zxcvbnm'] += 1
            
            total = 0
            for k,v in my_dict.items():
                if v == 0:
                    total += 1

            if total == 2: # two rows have no entries
                out.append(word)

        return out