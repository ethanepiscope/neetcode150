# O(n log m) time, O(1) space, where n is the number of piles and m is the maximum pile size.
# Once I realized k was bounded, used binary search to find the minimum k such that all bananas can be eaten in h hours or less

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_l = 1 #smallest reasonable value of k
        k_r = max(piles) #largest reasonable value of k
        while k_r > k_l:
            k_mid = (k_l + k_r)//2
            total = 0 #time to eat all piles with rate of k_mid
            for p in piles:
                total += p//k_mid + (p%k_mid != 0) #ceil of p/k_mid
            if total <= h:
                k_r = k_mid
            else:
                k_l = k_mid + 1
        return k_l