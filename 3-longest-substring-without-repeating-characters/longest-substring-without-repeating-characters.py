class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        charSet = set()
        l = 0
        ans = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            ans = max(ans, r-l+1)
            charSet.add(s[r])
        return ans
                
            