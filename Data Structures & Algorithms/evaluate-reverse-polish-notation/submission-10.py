class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        for ch in tokens:
            if ch not in operations:
                stack.append(int(ch))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(operations[ch](a, b))
        
        return stack[-1]