class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        out = [0]*k
        # for u in list(set([x[0] for x in logs])):
        #     uam = len(set([x[1] for x in logs if u==x[0]]))
        #     out[uam-1] += 1
        # return out

        myd = OrderedDict()
        for l in logs:
            user = l[0]
            action = l[1]
            
            if user not in myd.keys():
                myd[user] = set()
            myd[user].add(action)
        
        for mins in myd.values():
            uam = len(mins)
            out[uam-1] += 1
        return out
