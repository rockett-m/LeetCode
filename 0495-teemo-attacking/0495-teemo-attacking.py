class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        count = 0
        if len(timeSeries) == 1:
            return duration
        
        prev = -1
        for i in range(len(timeSeries)):
            
            curr = timeSeries[i]
            if prev != -1:
                if curr - prev >= duration:
                    
                    count += duration
                else:
                    count += curr - prev
            
            prev = curr
            
        return count + duration