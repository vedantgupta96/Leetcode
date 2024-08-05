class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] != nums[i-1] or i == 0:
                self.twoSum(i,nums,ans)
        return ans

    def twoSum(self,i,nums,ans):
        start,end = i+1, len(nums)-1
        while start < end:
            sums = nums[i] + nums[start] + nums[end]
            if sums > 0:
                end -= 1
            elif sums < 0:
                start += 1
            else:
                ans.append([nums[i],nums[start],nums[end]])
                start += 1
                end -= 1
                while nums[start] == nums[start-1] and start < end:
                    start += 1