class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:#the list is sorted so if 1st element is greater than 0 then there is no way to find a solution since all other values will also be greater than 0
                break
            if i==0 or nums[i-1] != nums[i]:
                self.twoSum(nums,i,ans)
        return ans
    def twoSum(self,nums,i,ans):
        start,end = i+1,len(nums)-1
        while start < end:
            sum = nums[start] + nums[i] + nums[end]
            if sum > 0:
                end-=1
            elif sum < 0:
                start += 1
            else:#don't forget to start+1 and end-1, also the while loop to increase start till we get a different value since duplicates are not allowed
                ans.append([nums[i],nums[start],nums[end]])
                start+=1
                end-=1
                while start<end and nums[start] == nums[start-1]:
                    start += 1
