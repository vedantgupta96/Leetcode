class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow=fast=nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        
        fast = nums[0]
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        
        
