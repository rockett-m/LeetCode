class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        new = []
        for idx, val in enumerate(image):
            temp = val[::-1]
            temp = [ 1^x for x in temp ]
            new.append(temp)
        return new
