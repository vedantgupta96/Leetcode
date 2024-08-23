class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i in range(len(nums)):
            numToFind = target - nums[i]
            if numToFind in temp:
                return [i, temp[numToFind]]
            else:
                temp[nums[i]] = i
        