class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # stores indices

        for i in range(len(temperatures)):
        # pop indices that have found their warmer day
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
        
            stack.append(i)

    # remaining indices in stack never found a warmer day
    # result is already 0 for them by default

        return result