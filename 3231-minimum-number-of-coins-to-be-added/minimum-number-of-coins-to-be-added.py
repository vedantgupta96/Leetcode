class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        ans, num, i = 0,0,0
        coins.sort()
        while num < target:
            if i < len(coins) and coins[i] <= num+1:
                num += coins[i]
                i+=1
            else:
                ans += 1
                num += num+1
        return ans


        