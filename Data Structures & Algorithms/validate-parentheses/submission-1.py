class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        maping = {"(": ")", "{": "}", "[": "]"}

        for ch in s:

            if ch in maping: # скобка открывающая
                stack.append(ch)

            elif len(stack) == 0: # скобка закрывающая и стек пуст
                return False
            
            else:            # скобка закрывающая и стек не пустой
                last_ch = stack.pop()
                if maping[last_ch] != ch:

                    return False
        
        return len(stack) == 0

        