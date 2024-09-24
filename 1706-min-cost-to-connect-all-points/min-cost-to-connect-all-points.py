class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        distMap = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                manDist = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                distMap[i].append([manDist,j])
                distMap[j].append([manDist,i])
        ans = 0
        visit = set()
        minH = [[0,0]]
        while len(visit) < len(points):
            cost , i = heapq.heappop(minH)
            if i in visit:
                continue
            visit.add(i)
            ans += cost
            for nCost,n in distMap[i]:
                if n not in visit:
                    heapq.heappush(minH,[nCost,n])
        return ans



        
        