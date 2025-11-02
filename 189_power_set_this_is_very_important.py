"""
Power Set

Generate all subsets (power set) of given array.

Time Complexity: O(2^n * n)
Space Complexity: O(2^n * n)
"""

from typing import List


def solve(
    v: List[int],
    index: int,
    subset: List[int],
    ans: List[List[int]]
) -> None:
    """
    Generate all subsets using backtracking.
    
    Args:
        v: Input array
        index: Current index
        subset: Current subset being built
        ans: List to store all subsets
    """
    if index == len(v):
        ans.append(subset[:])
        return
    
    # Include current element
    subset.append(v[index])
    solve(v, index + 1, subset, ans)
    
    # Exclude current element
    subset.pop()
    solve(v, index + 1, subset, ans)


def pwset(v: List[int]) -> List[List[int]]:
    """
    Generate power set of array.
    
    Args:
        v: Input array
        
    Returns:
        List of all subsets
    """
    ans = []
    solve(v, 0, [], ans)
    return ans

