class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost): return -1
        
        startStation, tank = 0, 0

        # reversed as closest to end of clockwise is desirable
        for idx, val in enumerate(gas):
            
            tank += gas[idx] - cost[idx]
            
            if tank < 0:
                # potential streak start \/
                startStation = idx + 1
                tank = 0
            
        return startStation
