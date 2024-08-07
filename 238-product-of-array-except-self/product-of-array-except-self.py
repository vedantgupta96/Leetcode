class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        pre,post = 1,1
        for i in range(len(nums)):
            answer[i] *= pre
            pre *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            answer[i] *= post
            post *= nums[i]
        return answer