# O(n + m) time complexity, O(1) space complexity since there are only 26 letters
# I didn't realize I could just use == for dictionaries which would have saved some time

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for c in s: #O(n)
            if c not in s_dict.keys(): #O(1) per iter
                s_dict[c] = 0 #O(1) per iter
            s_dict[c] += 1 #O(1) per iter
        for c in t: #O(m)
            if c not in s_dict.keys(): #O(1) per iter
                return False
            s_dict[c] -= 1 #O(1) per iter
        for v in s_dict.values(): #O(n)
            if v != 0: #O(1) per iter
                return False
        return True