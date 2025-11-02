"""
Greedy Algorithm to Find Minimum Number of Coins

Find minimum coins needed to make given amount using Indian currency.

Time Complexity: O(amount)
Space Complexity: O(1)
"""


def find_minimum_coins(amount: int) -> int:
    """
    Find minimum coins using greedy algorithm.
    
    Uses Indian currency denominations: [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    
    Args:
        amount: Target amount
        
    Returns:
        Minimum number of coins needed
    """
    denominations = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    count = 0
    i = 0
    
    while i < len(denominations):
        if denominations[i] <= amount:
            amount -= denominations[i]
            count += 1
        else:
            i += 1
    
    return count

