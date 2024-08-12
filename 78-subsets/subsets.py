class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        subset = []

        def dfs(n):
            if n >= len(nums):
                ans.append(subset.copy())
                return
            dfs(n+1)
            subset.append(nums[n])
            dfs(n+1)
            subset.pop()
            
        dfs(0)
        return ans
        