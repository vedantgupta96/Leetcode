class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        rev = 0
        if x < 0:
            return False
        while x:
            digit = int(math.fmod(x,10))
            x = int(x/10)
            rev = rev*10+digit
            print(rev)
        return rev == temp
