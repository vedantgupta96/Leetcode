class Solution:
    def maxArea(self, height: List[int]) -> int:
        start,end,maxArea = 0,len(height)-1,0

        while start < end:
            area = (end-start)*min(height[start],height[end])
            maxArea = max(area,maxArea)
            if height[start] > height[end]:
                end-=1
            else:
                start+=1
        return maxArea