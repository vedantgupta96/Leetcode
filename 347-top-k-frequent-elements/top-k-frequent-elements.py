class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        c = [(-v,k) for k,v in c.items()]
        print(c)
        heapq.heapify(c)
        print(c)
        output = []
        for i in range(k):
            item = heapq.heappop(c)
            output.append(item[1])
        return output
        