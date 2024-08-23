class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i],speed[i]))
        pairs.sort(reverse = True)
        for p,s in pairs:
            time = (target-p)/s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)

