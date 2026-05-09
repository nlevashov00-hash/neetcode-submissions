class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        numbers = []

        operations = {
            "+": lambda a, b: a + b, 
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)   
        }

        for ch in tokens:
            if ch not in operations:
                numbers.append(int(ch))
            else:
                b = numbers.pop()
                a = numbers.pop()
                numbers.append(operations[ch](a, b))
        
        return numbers[-1]

