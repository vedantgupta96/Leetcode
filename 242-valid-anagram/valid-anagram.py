class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first, second = {},{}
        for i in s:
            if i in first:
                first[i] += 1
            else:
                first[i] = 1
        for i in t:
            if i in second:
                second[i] += 1
            else:
                second[i] = 1
        return first == second