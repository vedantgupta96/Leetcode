class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        
        count = [(-v,k) for (k,v) in count.items()]
        heapq.heapify(count)
        output = []
        for i in range(k):
            item = heapq.heappop(count)
            output.append(item[1])
        return output

