# O(ElogE) time, where E is the number of tickets. O(E) space to store the graph.

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets,reverse=True):
            adj[src].append(dst)

        res = []
        stack = ["JFK"]
        while stack:
            cur = stack[-1]
            if len(adj[cur]) == 0:
                res.append(stack.pop())
            else:
                stack.append(adj[cur].pop())
        return res[::-1]