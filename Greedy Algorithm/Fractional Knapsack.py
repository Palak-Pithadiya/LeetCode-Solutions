class Solution:
    def fractionalKnapsack(self, val, wt, cap):
        # Your code goes here
        total = 0
        i = 0
        while i < len(wt):
            if cap - wt[i] < 0:
                temp = (cap * val[i]) / wt[i]
                total += temp 
                return total
            else:
                cap -= wt[i]
                total +=  val[i]

            i += 1

        return total
