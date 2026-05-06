class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        numbers = []

        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        for ch in tokens:

            if ch not in operators:
                numbers.append(int(ch))
            else:
                b = int(numbers.pop())
                a = int(numbers.pop())
                numbers.append(operators[ch](a, b))

        return numbers[0]

