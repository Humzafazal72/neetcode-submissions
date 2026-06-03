class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)

        for i,t in enumerate(temperatures):
            print(stack)
            while stack and stack[-1][0] < t:
                top = stack.pop()
                result[top[1]] = i-top[1]
            
            stack.append((t,i))
        
        return result