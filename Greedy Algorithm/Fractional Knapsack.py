class Solution:
    def fractionalKnapsack(self, val, wt, cap):
        # Your code goes here
        items = []
        for i in range(len(val)):
            ratio = val[i] / wt[i]
            items.append(val[i], wt[i], ratio)

        items.sorted(key=lambda x = x[:2], reversed = True)
        total_value = 0.0        
        
        for v, w, r in items:
            if cap < 0:
                break
            if cap - wt[i] >= 0:
                cap -= w
                total_value += v
            else:
                fractional_val = cap * r
                total_value += fractional_val
                cap = 0  # Bag is now full
                break

        return total_value
            
