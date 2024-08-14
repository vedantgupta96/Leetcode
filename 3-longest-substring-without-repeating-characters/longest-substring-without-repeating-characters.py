class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,ans,temp=0,0,0,[]

        while r < len(s):
            while s[r] in temp:
                temp.remove(s[l])
                l+=1
            temp.append(s[r])
            ans = max(ans,r-l+1)
            r+=1
        return ans
