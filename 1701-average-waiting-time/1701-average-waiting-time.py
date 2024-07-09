class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        if len(customers) < 2: return 0
        
        total_wait, prev_finish = 0, 0
        for idx, customer in enumerate(customers):
            arrival, task_time = customer
            
            wait = max(0, prev_finish - arrival)
            
            total_wait += wait + task_time
            prev_finish = wait + arrival + task_time

        return total_wait / len(customers)