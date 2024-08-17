class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = defaultdict(list)
        seen = set()
        seen.add(source)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(i):

            if i == destination:
                return True
            seen.add(i)
            for nei_node in graph[i]:
                if nei_node not in seen and dfs(nei_node):
                    return True
                        
            return False
        return dfs(source)

        