class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [[p,s] for p,s in zip(position,speed)]
        stack = []
        
        arr.sort(reverse = True)
        print(arr)
        for p,s in arr:
            timeToReachTarget = (target - p)/s
            if not stack or stack[-1]<timeToReachTarget:
                stack.append(timeToReachTarget)
        return len(stack)