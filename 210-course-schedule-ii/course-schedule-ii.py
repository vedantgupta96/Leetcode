class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visit,cycle = set(),set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return output

        



        