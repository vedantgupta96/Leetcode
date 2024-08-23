class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0]*len(temperatures)
        for n in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[n]:
                answer[stack[-1][1]] = n-stack[-1][1]
                stack.pop()
            stack.append((temperatures[n],n))
        return answer
            
