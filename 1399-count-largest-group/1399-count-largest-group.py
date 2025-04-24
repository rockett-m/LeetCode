class Solution:
    def countLargestGroup(self, n: int) -> int:
        high = 1
        mydict = {}
        for i in range(1, n+1):
            s = str(i)
            summ = sum([int(s[z]) for z in range(len(s))])

            if summ not in mydict:
                mydict[summ] = [i]
            else:
                mydict[summ].append(i)
                high = max(high, len(mydict[summ]))

        # work with high - longest length
        count = 0
        for k,v in mydict.items():
            if len(v) == high:
                count += 1
    
        return count
