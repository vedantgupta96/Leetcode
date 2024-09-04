class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        stack = [(0, [])]  # Stack to hold (index, current subset)

        while stack:
            index, subset = stack.pop()

            # If we've processed all elements, add the subset to the result
            if index == len(nums):
                ans.append(subset)
            else:
                # Decision to include nums[index] in the subset
                stack.append((index + 1, subset + [nums[index]]))
                # Decision to exclude nums[index] from the subset
                stack.append((index + 1, subset))

        return ans
