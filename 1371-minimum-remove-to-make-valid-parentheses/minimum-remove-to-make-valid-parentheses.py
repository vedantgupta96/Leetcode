class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        indexSet = set()

        for i in range(len(s)):
            if s[i] != ')' and s[i] != '(':
                continue
            if s[i] == '(':
                stack.append(i)
            elif len(stack) == 0:
                indexSet.add(i)
            else:
                stack.pop()
        indexSet = indexSet.union(set(stack))
        ans = []
        for i in range(len(s)):
            if i not in indexSet:
                ans.append(s[i])
        return "".join(ans)
        
        