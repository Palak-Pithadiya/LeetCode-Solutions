class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        
        strs = s + s

        is_rotation = False

        if goal in strs:
            is_rotation = True

        return is_rotation

s = "abcde"
goal = "cdeab"
obj = Solution()
print(obj.rotateString(s, goal))
