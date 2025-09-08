# O(n) time, O(m) space, where n is the length of the given string and m is the number of unique characters in the string.



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charFreq = defaultdict(int)  #map characters to their frequency in the window
        start, current = 0, 0 #idx's, inclusive
        maxLen = 0
        maxFreq = 0
        while current < len(s):
            charFreq[s[current]] += 1 #tentatively add s[current] to window
            maxFreq = max(maxFreq, charFreq[s[current]]) #only need to update maxFreq when it increases
            if maxFreq < current - start + 1 - k: #check to see if window is valid
                charFreq[s[start]] -= 1 #if not, slide window
                start += 1
            maxLen = max(maxLen, current - start + 1)
            current += 1
        return maxLen