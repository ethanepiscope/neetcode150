#Pretty simple O(n) solution, Unchanged when redoing it

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = "abcdefghijklmnopqrstuvwxyz1234567890"
        s = s.lower()
        start = 0
        end = len(s)-1
        while start < end:
            if s[start] not in alphanumeric:
                start += 1
            if s[end] not in alphanumeric:
                end -= 1
            if s[start] in alphanumeric and s[end] in alphanumeric:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
        return True