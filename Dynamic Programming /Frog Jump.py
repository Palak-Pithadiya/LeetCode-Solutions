class Solution:
    def frogJump(self, heights):
        n = len(heights)

        prev2 = 0
        prev1 = abs(heights[1] - heights[0])

        for i in range(2, n):
            jump_one = prev1 + abs(heights[i] - heights[i-1])
            jump_two = prev2 + abs(heights[i] - heights[i-2])
            curr = min(jump_one, jump_two)

            prev2 = prev1
            prev1 = curr
        return prev1
