"""
Chess Tournament

Allocate minimum distance between players such that all can be placed.

Time Complexity: O(n log(max_distance))
Space Complexity: O(1)
"""

from typing import List
import sys


def is_possible(mid: int, positions: List[int], c: int) -> bool:
    """
    Check if allocation is possible with given minimum distance.
    
    Args:
        mid: Minimum distance between players
        positions: Sorted positions
        c: Number of players
        
    Returns:
        True if possible, False otherwise
    """
    count = 1
    last_pos = positions[0]
    
    for pos in positions:
        if pos - last_pos >= mid:
            count += 1
            if count == c:
                return True
            last_pos = pos
    
    return False


def chess_tournament(positions: List[int], n: int, c: int) -> int:
    """
    Find maximum minimum distance between players.
    
    Args:
        positions: Positions available
        n: Number of positions
        c: Number of players
        
    Returns:
        Maximum minimum distance
    """
    positions.sort()
    low = 1
    high = max(positions) - min(positions)
    ans = -1
    
    while low <= high:
        mid = low + (high - low) // 2
        if is_possible(mid, positions, c):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return ans

