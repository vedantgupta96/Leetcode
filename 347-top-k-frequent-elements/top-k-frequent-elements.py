class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        c = [(-v,k) for k,v in c.items()]
        heapq.heapify(c)
        output = []
        for i in range(k):
            output.append(heapq.heappop(c)[1])
        return output
        