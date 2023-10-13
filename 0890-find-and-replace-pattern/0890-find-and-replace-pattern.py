class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        assn = 1        
        match = []
        my_dict = OrderedDict()
        for let in pattern:
            if let not in my_dict.keys():
                my_dict[let] = assn
                assn += 1
            match.append(my_dict[let])
        
        options = []
        for w in words:
            numbers = []
            my_d = OrderedDict()
            start = 1
            for y in w:
                if y not in my_d.keys():
                    my_d[y] = start
                    start += 1
                numbers.append(my_d[y])
            if match == numbers:
                options.append(w)
            
        return options