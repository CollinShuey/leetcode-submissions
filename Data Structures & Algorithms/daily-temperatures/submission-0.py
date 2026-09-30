class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []#pairs
        output = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            if not stack or temp <= stack[-1][0]:
                stack.append([temp,i])
            else:
                while stack and temp > stack[-1][0]:
                    past = stack.pop()
                    output[past[1]] = i - past[1]
                stack.append([temp,i])
        return output


        