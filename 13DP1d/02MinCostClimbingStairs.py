# O(n) time and O(n) space, where n is the length of cost.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        minCost = [0] * n #memoize the min cost to top from stair i
        minCost[n-1] = cost[n-1]
        minCost[n-2] = cost[n-2]
        for i in range(n-3,-1,-1):
            minCost[i] = cost[i] + min(minCost[i+1],minCost[i+2])
        return min(minCost[0],minCost[1])
        