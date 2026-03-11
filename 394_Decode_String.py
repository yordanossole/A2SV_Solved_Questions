# leetcode
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                substr = []
                while stack[-1] != '[':
                    substr.append(stack.pop())

                stack.pop()

                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())

                num = int("".join(num[::-1]))
                substr = "".join(substr[::-1])
                stack.append(substr*num)
        
        return "".join(stack)