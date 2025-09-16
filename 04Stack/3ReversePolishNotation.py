# O(n) time, O(n) space, where n is the length of the given tokens list. Used a stack to store numbers for later operations.


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            print(nums)
            if token == "+":
                arg2 = nums.pop()
                arg1 = nums.pop()
                nums.append(arg1+arg2)
            elif token == "-":
                arg2 = nums.pop()
                arg1 = nums.pop()
                nums.append(arg1-arg2)
            elif token == "*":
                arg2 = nums.pop()
                arg1 = nums.pop()
                nums.append(arg1*arg2)
            elif token == "/":
                arg2 = nums.pop()
                arg1 = nums.pop()
                nums.append(int(arg1/arg2))
            else: #number
                nums.append(int(token))
        return nums[0]