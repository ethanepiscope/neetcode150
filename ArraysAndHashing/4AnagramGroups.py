# O(mn) time, O(m) space. This is gross and would be better if I used ord() to get unicode values and a size 26 array to represent the dict.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {} #map freq map tuple to list of strings
        for s in strs: # O(m)
            freq_map = {}
            for c in s: #create the freq map in O(n) time
                freq_map[c] = 1 + freq_map.get(c, 0)
            key = tuple(sorted(freq_map.items())) #O(1) per iter since freq map has at most 26 entries
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
        return list(d.values())