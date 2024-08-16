class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = []
        def dfs(i, total):
            if total == target:
                ans.append(cur.copy())
                return
            if i == len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i,total+candidates[i])
            cur.pop()
            dfs(i+1,total)
            return
        dfs(0,0)
        return ans
            
        