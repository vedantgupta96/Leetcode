class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sol = []
        nums.sort()

        def dfs(i):
            if i == len(nums):
                ans.append(sol.copy())
                return
            sol.append(nums[i])
            dfs(i+1)
            sol.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1)
        dfs(0)
        return ans
        