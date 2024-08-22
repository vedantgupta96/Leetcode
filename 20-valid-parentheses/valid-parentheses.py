class Solution:
    def isValid(self, s: str) -> bool:

        ans = []
        paren = {')':'(',']':'[','}':'{'}

        for c in s:
            if c not in paren:
                ans.append(c)
            elif not ans or paren[c] != ans.pop():
                return False
        return not ans