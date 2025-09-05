# Dijkstra's algorithm. O(E log V) time, where E is number of edges and V is number of vertices
# O(V+E) space

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        neighbors = {} #map node to neighboring nodes, cost
        prioQueue = [] #search frontier
        visited = set()
        maxCost = 0
        for (u,v,t) in times:
            if u not in neighbors:
                neighbors[u] = []
            neighbors[u].append((v,t))
        heapq.heappush(prioQueue, (0, k))
        while prioQueue:
            cost, node = heapq.heappop(prioQueue)
            if node in visited:
                continue
            visited.add(node)
            maxCost = cost
            if node in neighbors:
                for (v,t) in neighbors[node]:
                    if v not in visited:
                        heapq.heappush(prioQueue, (t+cost, v))
        if len(visited) == n:
            return maxCost
        return -1
