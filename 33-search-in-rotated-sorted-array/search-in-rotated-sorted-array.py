class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l<r:
            mid = (l+r)//2
            if nums[r] < nums[mid]:
                l = mid+1
            else:
                r = mid
        min_index = r
        if min_index == 0:
            l=0
            r=len(nums)-1
        elif target>=nums[0] and target <= nums[min_index-1]:
            l = 0 
            r=min_index-1
        else:
            l = min_index
            r = len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid+1
            else:
                r = mid-1
            
        return -1