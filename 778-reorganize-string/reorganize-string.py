class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(-count,char) for char,count in count.items()]
        heapq.heapify(heap)
        ans = []
        if len(s) == 1:
            return s

        while len(heap) >= 2:
            top_count, top_char = heapq.heappop(heap)
            next_count, next_char = heapq.heappop(heap)

            ans.append(top_char)
            ans.append(next_char)
            
            if top_count +1:
                heapq.heappush(heap,(top_count+1,top_char))
            if next_count +1:
                heapq.heappush(heap,(next_count+1,next_char))
        
        if heap:
            count, char = heapq.heappop(heap)
            if count != -1 or char == ans[-1]:
                return ""
            else:
                ans.append(char)
        if ans:
            return "".join(ans)
        else:
            return ""

        