from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Track the lowest price encountered
        max_profit = 0  # Maximum profit initialized to 0

        for price in prices:
            if price < min_price:
                min_price = price  # Update lowest price
            profit = price - min_price  # Profit if selling today
            max_profit = max(max_profit, profit)  # Update max profit
        
        return max_profit  # Return the best profit found
