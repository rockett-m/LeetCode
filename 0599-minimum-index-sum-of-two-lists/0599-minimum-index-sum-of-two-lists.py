class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        minn = -1
        word = []
        
        for idx, val in enumerate(list1):
            if val in list2:
                summ = idx + list2.index(val)
                if summ == minn:
                    word.append(val)

                if summ < minn or minn < 0:
                    minn = summ
                    word = []
                    word.append(val)
        return word