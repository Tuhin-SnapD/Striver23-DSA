"""
Online Stock Span

Calculate span of stock price for each day (number of consecutive days
including current day where price was <= current price).

Time Complexity: O(n) amortized
Space Complexity: O(n)
"""

from typing import List


def find_spans(price: List[int]) -> List[int]:
    """
    Find stock span for each day.
    
    Args:
        price: Stock prices for each day
        
    Returns:
        Spans for each day
    """
    stack = []  # Stack of (price, span)
    result = [0] * len(price)
    
    for i in range(len(price)):
        span = 1
        
        # Accumulate spans of previous days with lower prices
        while stack and stack[-1][0] <= price[i]:
            span += stack[-1][1]
            stack.pop()
        
        stack.append((price[i], span))
        result[i] = span
    
    return result

