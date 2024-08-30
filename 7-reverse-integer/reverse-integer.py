class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31
        MAX = 2**31 -1
        ans = 0

        while x:
            digit = int(math.fmod(x,10))
            x = int(x/10)

            if(ans > MAX//10) or (digit > MAX%10 and ans == MAX//10):
                return 0
            if(ans < MIN//10) or (digit < MAX%10 and ans == MIN//10):
                return 0
            ans = (ans*10)+digit

        return ans
        