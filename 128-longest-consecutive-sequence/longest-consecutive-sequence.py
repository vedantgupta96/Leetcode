class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = 1
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        x = set(nums)
        for i in x:
            if i-1 not in x:
                j = 1
                while i+j in x:
                    num = max(num,j+1)
                    j += 1
        return num
                


        