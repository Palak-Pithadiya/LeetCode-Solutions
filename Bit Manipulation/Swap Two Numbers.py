class Solution:
    def swap(self, a, b):
        """
        Swap two integers and return them.

        Args:
            a (int): First integer.
            b (int): Second integer.

        Returns:
            Tuple[int, int]: The two integers, swapped.
        """
        a = a ^ b
        b = a ^ b
        a = a ^ b
      
        return a, b

"""a = 5, b = 10
a = a + b | a = 15
b = a - b | b = 5 
a = a - b | a = 15 - 5 = 10
OR
temp = a
a = b
b = temp"""

