"""
Find Nth Root of M

Find nth root of m using binary search.

Time Complexity: O(log(m) * log(n))
Space Complexity: O(1)
"""


def nth_root(n: int, m: int) -> int:
    """
    Find nth root of m using binary search.
    
    Args:
        n: Root degree
        m: Number
        
    Returns:
        Nth root if exists, -1 otherwise
    """
    low = 1
    high = m
    
    while low <= high:
        mid = low + (high - low) // 2
        
        power = mid ** n
        
        if power == m:
            return mid
        elif power > m:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1

