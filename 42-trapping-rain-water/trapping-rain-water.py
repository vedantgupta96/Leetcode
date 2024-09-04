class Solution:
    def trap(self, height: List[int]) -> int:
        totalWater = 0
        l,r = 0,len(height)-1
        leftMax = height[l]
        rightMax = height[r]
        
        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax,height[l])
                totalWater += leftMax - height[l]
            else:
                r-=1
                rightMax = max(rightMax,height[r])
                totalWater += rightMax - height[r]
        return totalWater

        # ans = 0
        # size = len(height)
        # for i in range(1, size - 1):
        #     left_max = 0
        #     right_max = 0
        #     # Search the left part for max bar size
        #     for j in range(i, -1, -1):
        #         left_max = max(left_max, height[j])
        #     # Search the right part for max bar size
        #     for j in range(i, size):
        #         right_max = max(right_max, height[j])
        #     ans += min(left_max, right_max) - height[i]
        # return ans