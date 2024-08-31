class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = currGas = start = 0

        for i in range(len(gas)):
            totalGas += gas[i] - cost[i]
            currGas += gas[i] - cost[i]
            if currGas < 0:
                currGas = 0
                start = i+1
        return start if totalGas>=0 else -1
        