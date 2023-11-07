class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        paired = [0 for x in words]
        my_dict = OrderedDict()
        count = 0
        for idx, key in enumerate(words):
            my_dict[key] = []
            for ix, w in enumerate(words):
                if ix > idx and w[::-1] == key:
                    my_dict[key].append(w)
                    count += 1
        # print(my_dict)
        # totals = Counter(my_dict.values())
        # print(totals)
        # count = 0
        # for i in totals:
        #     if i > 0: count += i
        return count