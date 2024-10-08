class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        stack = [(0,[])]
        nums.sort()

        while stack:
            index, subset = stack.pop()
            
            if index == len(nums):
                ans.append(subset)
            else:
                stack.append((index+1,subset+[nums[index]]))
                while index+1 < len(nums) and nums[index] == nums[index+1]:
                    index+=1
                stack.append((index+1,subset))
            
        return ans
        # ans = []
        # sol = []
        # nums.sort()

        # def dfs(i):
        #     if i == len(nums):
        #         ans.append(sol.copy())
        #         return
        #     sol.append(nums[i])
        #     dfs(i+1)
        #     sol.pop()
        #     while i+1 < len(nums) and nums[i] == nums[i+1]:
        #         i+=1
        #     dfs(i+1)
        # dfs(0)
        # return ans
        