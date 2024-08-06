class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l < r:
            mid = (r+l)//2
            if nums[r] < nums[mid]:
                l = mid+1
            else:
                r = mid
        min_index = r
        if min_index == 0:
            l,r = 0, len(nums)-1
        elif target >= nums[0] and target <= nums[min_index-1]:
            l,r = 0, min_index-1
        else:
            l, r = min_index, len(nums)-1
        while r>=l:

            mid = (r+l)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return -1