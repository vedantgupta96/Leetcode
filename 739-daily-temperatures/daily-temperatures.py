class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack = []
        # answer = [0]*len(temperatures)
        # for n in range(len(temperatures)):
        #     while stack and stack[-1][0] < temperatures[n]:
        #         i = stack.pop()[1]
        #         answer[i] = n-i
        #     stack.append((temperatures[n],n))
        # return answer

        n = len(temperatures)
        hottest = 0
        answer = [0] * n
        
        for curr_day in range(n - 1, -1, -1):
            current_temp = temperatures[curr_day]
            if current_temp >= hottest:
                hottest = current_temp
                continue
            
            days = 1
            while temperatures[curr_day + days] <= current_temp:
                # Use information from answer to search for the next warmer day
                days += answer[curr_day + days]
            answer[curr_day] = days

        return answer
            
