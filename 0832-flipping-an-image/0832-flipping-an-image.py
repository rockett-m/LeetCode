class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        new = []
        for idx, val in enumerate(image):
            temp = [ 1^x for x in val[::-1] ]
            new.append(temp)
        return new
