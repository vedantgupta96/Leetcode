class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        cur = []

        def backtrack():
            if len(cur) == len(nums):
                ans.append(cur.copy())
                return

            for i in nums:
                if i not in cur:
                    cur.append(i)
                    backtrack()
                    cur.pop()
        backtrack()
        return ans