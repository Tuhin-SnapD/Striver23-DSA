"""
Longest Common Prefix

Find longest common prefix among array of strings.

Time Complexity: O(n * m) where n is number of strings, m is length
Space Complexity: O(1)
"""

from typing import List


def longest_common_prefix(arr: List[str], n: int) -> str:
    """
    Find longest common prefix.
    
    Args:
        arr: Array of strings
        n: Number of strings
        
    Returns:
        Longest common prefix string
    """
    if n == 0:
        return ""
    
    arr.sort()
    first = arr[0]
    last = arr[n - 1]
    
    result = ""
    min_len = min(len(first), len(last))
    
    for i in range(min_len):
        if first[i] == last[i]:
            result += first[i]
        else:
            break
    
    return result

