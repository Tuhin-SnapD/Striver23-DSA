"""
Fractional Knapsack

Maximize value by selecting items with fractional amounts allowed.

Time Complexity: O(n log n) due to sorting
Space Complexity: O(1)
"""

from typing import List, Tuple


def maximum_value(items: List[Tuple[int, int]], n: int, w: int) -> float:
    """
    Find maximum value using fractional knapsack.
    
    Items are (weight, value) pairs.
    Uses greedy: sort by value/weight ratio and take items accordingly.
    
    Args:
        items: List of (weight, value) pairs
        n: Number of items
        w: Weight capacity
        
    Returns:
        Maximum value achievable
    """
    # Sort by value/weight ratio (descending)
    items.sort(key=lambda x: x[1] / x[0], reverse=True)
    
    result = 0.0
    
    for weight, value in items:
        if weight <= w:
            # Take full item
            result += value
            w -= weight
        else:
            # Take fraction of item
            result += value * (w / weight)
            break
    
    return result

