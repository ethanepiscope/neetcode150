#O(m) time, O(m+n) space. m is sum of lengths of all strings and n is number of strings

class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret += str(len(s)) + ':' + s
        return ret

    def decode(self, s: str) -> List[str]:
        i = 0 #starts of sequences
        j = 1 #ends of sequences
        ret = []
        while i < len(s):
            if s[j] != ':':
                j += 1
            else:
                length = int(s[i:j])
                ret.append(s[j+1:j+1+length])
                i = j+1+length
                j = i + 1
        return ret
