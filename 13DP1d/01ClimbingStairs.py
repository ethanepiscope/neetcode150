# Top down DP approach. O(n) time and space

class Solution:
    def climbStairs(self, n: int) -> int:
        numsteps = [0 for num in range(n+1)] # memoize num steps from position i
        numsteps[n] = 1
        numsteps[n-1] = 1
        for i in range(n-2,-1,-1):
            numsteps[i] = numsteps[i+1] + numsteps[i+2]
        return numsteps[0]