class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append([value,timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        curr = self.dict[key]
        l,r = 0,len(curr)-1
        ans = ''
        # l = curr[0][1]
        # r = curr[-1][1]
        while l<=r:
            mid = (l+r)//2

            if timestamp >= curr[mid][1]:
                ans = curr[mid][0]
                l = mid+1
            else:
                r = mid-1
        return ans
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)