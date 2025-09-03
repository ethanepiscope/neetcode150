# O(n) time, O(m) space where m is num of unique chars in s

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_window = set()
        i = 0 #left edge of window, inclusive
        j = 0 #right edge, not inclusive
        max_length = 0
        while j < len(s):
            if s[j] not in char_window:
                char_window.add(s[j])
                j += 1
                if j - i > max_length:
                    max_length = j - i
            else: #s[j] in char window
                char_window.remove(s[i])
                i += 1                    
        return max_length
                
