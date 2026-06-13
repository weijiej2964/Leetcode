class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force, for each index, loop forward to find warmer day
        #Use a stack, storing index
            #Loop through temperatures, check current index compared to top of stack
            #if current index is greater than top of stack keep poping it until its not
            # Add the current index into the stack
            #After loop ends, append len(stack) 0s solved by init arr size
        an = [0] * len(temperatures) 
        stack = deque()
        stack.append(0)

        for i in range(1,len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                an[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return an


