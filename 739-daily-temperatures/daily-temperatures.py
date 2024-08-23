class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0]*len(temperatures)
        for n in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[n]:
                i = stack.pop()[1]
                answer[i] = n-i
            stack.append((temperatures[n],n))
        return answer
            
