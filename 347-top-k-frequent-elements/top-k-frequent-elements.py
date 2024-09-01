class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}
        ans = []
        for i in range(len(nums)):
            if nums[i] not in countDict:
                countDict[nums[i]] = 1
            else:
                countDict[nums[i]] += 1
        countDict = [(-v,k) for k,v in countDict.items()]
        heapq.heapify(countDict)

        while k:
            ans.append(heapq.heappop(countDict)[1])
            k-=1
        return ans




