#O(n) time, O(n) space

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {} # map numbers to frequencies
        for num in nums: #O(n)
            freq_dict[num] = 1 + freq_dict.get(num, 0)
        freq_buckets = [[] for num in nums] # map frequencies to lists of numbers
        for num, freq in freq_dict.items(): #O(n)
            freq_buckets[freq-1].append(num)
        ret = []
        for num_list in freq_buckets[::-1]: #O(n) for the iteration and O(n) for the reversal
            for num in num_list:
                if k == 0:
                    break
                ret.append(num)
                k -= 1
        return ret
