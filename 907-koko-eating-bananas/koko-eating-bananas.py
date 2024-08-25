class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        ans = r

        while l <= r:
            hours = 0
            k = (l+r)//2
            for p in piles:
                hours += math.ceil(p/k)
            if hours>h:
                l=k+1
            else:
                ans = min(ans,k)
                r=k-1
        return ans
                
