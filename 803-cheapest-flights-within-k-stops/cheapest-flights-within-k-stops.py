class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = [float('inf')]*n
        price[src] = 0
        for i in range(k+1):
            tempPrice = price.copy()
            for source, dest, value in flights:
                if price[source] == float('inf'):
                    continue
                if price[source] + value < tempPrice[dest]:
                    tempPrice[dest] = price[source] + value
            price = tempPrice
        return -1 if price[dst] == float('inf') else price[dst]    