class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        aSeen,pSeen = set(),set()
        aQ,pQ = deque(),deque()
        m, n = len(heights),len(heights[0])

        for i in range(m):
            pSeen.add((i,0))
            pQ.append((i,0))
        
        for i in range(1,n):
            pSeen.add((0,i))
            pQ.append((0,i))

        for i in range(m):
            aSeen.add((i,n-1))
            aQ.append((i,n-1))
        
        for i in range(n-1):
            aSeen.add((m-1,i))
            aQ.append((m-1,i))
        
        def bfs(que,seen):
            coords = set()
            while que:
                x,y = que.popleft()
                coords.add((x,y))

                for i,j in [(0,1), (1,0) , (-1,0), (0,-1)]:
                    r,c = x+i,y+j
                    if 0<=r<m and 0<=c<n and heights[r][c]>=heights[x][y] and (r,c) not in seen:
                        seen.add((r,c))
                        que.append((r,c))
            return coords
        pCoords = bfs(pQ,pSeen)
        aCoords = bfs(aQ,aSeen)
        return pCoords.intersection(aCoords)


        

        