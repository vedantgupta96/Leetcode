class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}
        for c in s:
            if c in first:
                first[c] +=1
            else:
                first[c] = 1
        for c in t:
            if c in second:
                second[c] +=1
            else:
                second[c] = 1
        return first==second