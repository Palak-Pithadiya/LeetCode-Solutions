class Solution:
    def sortStack(self, stack):
        if not stack: return
        temp = stack.pop()
        self.sortStack(stack)
        self.insertInSortedWay(stack, temp)

    def insertInSortedWay(self, stack, element):
        if not stack or element > stack[-1]:
            stack.append(element)
            return

        temp = stack.pop()
        self.insertInSortedWay(stack, element)
        stack.append(temp)


obj = Solution()
print(obj.sortStack([4, 1, 3, 2]))
