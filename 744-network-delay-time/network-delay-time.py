class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {}

        for u,v,w in times:
            if u not in edges:
                edges[u] = []
            edges[u].append((v,w))
        
        minHeap = [(0,k)]
        time = 0
        visit = set()

        while minHeap:
            w1 , n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue
            
            visit.add(n1)
            time = max(w1,time)
            
            if n1 not in edges:
                continue

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap,(w1+w2,n2))
        return time if len(visit) == n else -1


        