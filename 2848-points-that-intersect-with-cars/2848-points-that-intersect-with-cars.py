class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
        cars = set()
        for i in nums:
            for j in range(i[0], i[1]+1):
                cars.add(j)
        
        return len(cars)