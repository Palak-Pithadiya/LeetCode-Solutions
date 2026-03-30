class Solution:
    def reverseStack(self, stack):
        # Your code goes here
        if not stack: return
        temp = stack.pop()
        self.reverseStack(stack)
        self.insertInStack(stack, temp)

    def insertInStack(self, stack, element):
        if not stack:
            stack.append(element)
            return

        temp = stack.pop()
        self.insertInStack(stack, element)
        stack.append(temp)
