class Solution:
    def alphaNum(self,s):
        if (ord('a') <= ord(s) <= ord('z')) or (ord('A') <= ord(s) <= ord('Z')) or (ord('0') <= ord(s) <= ord('9')):
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        start,end = 0, len(s)-1
        if not s:
            return True
        while start < end:
            while not self.alphaNum(s[start]) and start < end:
                start += 1
            while not self.alphaNum(s[end]) and start < end:
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
                
            
        