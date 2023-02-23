class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}
        for i in range(len(arr)):
            if arr[i] not in dict:
                dict[arr[i]] = 1
            else:
                if arr[i] in dict:
                    dict[arr[i]] += 1

        array = []
        for count in dict.values():
            if count not in array:
                array.append(count)
            else:
                return False

        return True
