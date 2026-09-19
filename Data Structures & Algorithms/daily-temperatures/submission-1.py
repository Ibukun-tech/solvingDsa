class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result= [0] * len(temperatures)
        stack = []
        for i, j in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < j:
                k = stack.pop()

                result[k]= i - k
            stack.append(i)
        return result