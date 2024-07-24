class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}

        for i,j in enumerate(nums):
            print(i,j)
            k = target - j
            if k in temp:
                return [i,temp[k]]
            else:
                temp[j]= i  