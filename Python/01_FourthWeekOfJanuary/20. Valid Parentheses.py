class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['(', '{', '[']
        close = [')', '}', ']']
        for com in s:
            if com in open:
                stack.append(com)
            elif com in close:
                if not stack:
                    return False
                if com == ')' and stack[-1] == '(':
                    stack.pop()
                elif com == ']' and stack[-1] == '[':
                    stack.pop()
                elif com == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False


## 책 풀이
def isValid(self, s: str) -> bool:
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False

    return len(stack) == 0