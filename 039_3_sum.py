"""
3Sum

Find all unique triplets that sum to target value.

Time Complexity: O(n^2)
Space Complexity: O(1) excluding output
"""

from typing import List


def find_triplets(arr: List[int], n: int, k: int) -> List[List[int]]:
    """
    Find all unique triplets that sum to k.
    
    Uses sorting and two-pointer technique.
    
    Args:
        arr: Array of integers
        n: Length of array
        k: Target sum
        
    Returns:
        List of unique triplets that sum to k
    """
    arr.sort()
    ans = []
    
    # Fix first element and use two-pointer for remaining two
    for i in range(n - 2):
        j = i + 1
        k_idx = n - 1
        
        while j < k_idx:
            current_sum = arr[i] + arr[j] + arr[k_idx]
            
            if current_sum == k:
                ans.append([arr[i], arr[j], arr[k_idx]])
                j += 1
                k_idx -= 1
            elif current_sum > k:
                k_idx -= 1
            else:
                j += 1
    
    # Remove duplicates
    unique_ans = []
    seen = set()
    for triplet in sorted(ans):
        triplet_tuple = tuple(triplet)
        if triplet_tuple not in seen:
            seen.add(triplet_tuple)
            unique_ans.append(list(triplet_tuple))
    
    return unique_ans

