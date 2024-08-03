class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}

        for i,num in enumerate(nums):
            k = target - num
            if k in temp:
                return [i,temp[k]]
            else:
                temp[num] = i
        