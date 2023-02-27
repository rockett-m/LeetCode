class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        my_dict = {}
        for idx, size in enumerate(groupSizes):
            if str(size) not in my_dict.keys():
                my_dict[str(size)] = [idx]
            else:
                my_dict[str(size)].append(idx)
        
        output = []
        for key, value in my_dict.items():
            temp = []

            for idx, elem in enumerate(value):
                temp.append(elem)

                if len(temp) >= int(key):
                    output.append(temp)
                    temp = []

        return output