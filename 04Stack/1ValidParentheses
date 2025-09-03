# O(n) time, O(n) space

class Solution:
    def isValid(self, s: str) -> bool:
        char_stack = []
        leftToRight = {"(" : ")", "[" : "]", "{" : "}"}
        for char in s:
            if char in leftToRight:
                char_stack.append(char)
            else:
                if not char_stack:
                    return False
                current = char_stack.pop()
                if char != leftToRight[current]:
                    return False
        return not char_stack #make sure its empty