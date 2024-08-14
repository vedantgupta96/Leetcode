class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        l,r=0,0
        s1Count,s2Count = [0]*26,[0]*26
        while r < len(s1):
            s1Count[ord(s1[r]) - ord('a')] += 1
            s2Count[ord(s2[r]) - ord('a')] += 1
            r += 1
        r -= 1
        while r < len(s2):
            if s1Count == s2Count:
                return True
            r+=1
            if r != len(s2):
                s2Count[ord(s2[r]) - ord('a')] += 1
            s2Count[ord(s2[l]) - ord('a')] -= 1
            l+=1
        return False