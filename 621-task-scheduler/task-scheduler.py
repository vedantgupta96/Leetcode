class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for i in range(len(tasks)):
            if tasks[i] not in count:
                count[tasks[i]] = 1
            else:
                count[tasks[i]] += 1
        nums = [-v for k,v in count.items()]
        heapq.heapify(nums)
        q = deque()
        time = 0

        while q or nums:
            time+=1
            if nums:
                cnt = 1 + heapq.heappop(nums)
                if cnt:
                    q.append((cnt,time+n))
            if q and q[0][1] == time:
                heapq.heappush(nums,q.popleft()[0])
        return time




