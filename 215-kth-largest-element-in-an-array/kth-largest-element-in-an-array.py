class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        
        nums = [-n for n in nums]
        heapq.heapify(nums)
        ans = -float('Inf')
        while k:
            
            ans = heapq.heappop(nums)
            k -= 1
        return -ans