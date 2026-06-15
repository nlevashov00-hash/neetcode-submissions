class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            
            while stack and temperatures[stack[-1]] < temperatures[i]:
                last_indx = stack.pop()
                result[last_indx] = i - last_indx
            stack.append(i)
        return result