class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0: return total_time

        c = Counter(tasks)
        
        def push_back(max_heap, occ, name):
            if occ != 0:
                heapq.heappush(max_heap, (occ, name))
            
        max_heap = []
        for k,v in c.items():
            max_heap.append((-v, k))
            
        heapq.heapify(max_heap)
        
        cool_queue = deque()
        
        time = 0
        # while either has items...keep time going
        while max_heap or cool_queue:
            # simulate 1 cycle
            time += 1
            
            if max_heap:
                occ, name = heapq.heappop(max_heap)
                occ *= -1
                occ -= 1

                if occ != 0:
                    # time when job finished
                    job_done_at = time + n
                    cool_queue.append((job_done_at, occ, name))
            
            # check FIFO queue first elem for time match, then pop
            if cool_queue and cool_queue[0][0] == time:
                job_done_at, occ, name = cool_queue.popleft()
                push_back(max_heap, -occ, name)

        return time
