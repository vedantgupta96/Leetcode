class Solution:

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move left pointer if not alphanumeric
            if not s[left].isalnum():
                left += 1
                continue
            
            # Move right pointer if not alphanumeric
            if not s[right].isalnum():
                right -= 1
                continue
            
            # Compare characters
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
                
            
        