class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distances = [float('inf')] * n
        distances[src] = 0
        for _ in range(k +1):
            temp = distances.copy()
            for u, v, cost in flights:
                if distances[u] != float("inf"):
                    temp[v]= min(temp[v], distances[u] + cost)
            distances = temp
        return distances[dst] if distances[dst] !=float('inf') else -1
        