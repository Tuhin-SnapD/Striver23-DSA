"""
Best Time to Buy and Sell Stock

Find the maximum profit from buying and selling a stock once.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def maximum_profit(prices: List[int]) -> int:
    """
    Calculate maximum profit from buying and selling stock once.
    
    Args:
        prices: List of stock prices
        
    Returns:
        Maximum profit achievable
    """
    max_profit = 0
    min_price = float('inf')
    
    for price in prices:
        # Track the minimum price seen so far
        min_price = min(min_price, price)
        
        # Calculate profit if we sell at current price
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

