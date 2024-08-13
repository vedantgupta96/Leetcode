class Solution:
    def maxArea(self, height: List[int]) -> int:
        start,end = 0, len(height)-1
        ans = 0

        while start < end:
            area = min(height[start],height[end])*(end-start)
            ans = max(area,ans)
            if height[start]>height[end]:
                end-=1
            else:
                start+=1
        return ans