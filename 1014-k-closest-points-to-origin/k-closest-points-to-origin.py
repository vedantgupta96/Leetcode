class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance, ans = [],[]

        for x,y in points:
            distance.append([(x**2+y**2),x,y])
        
        heapq.heapify(distance)
        while k:
            dist,x,y = heapq.heappop(distance)
            ans.append([x,y])
            k-=1
        return ans