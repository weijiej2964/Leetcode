class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = deque()
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            elif len(stack) != 0:
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack) > 0:
            return False
        return True