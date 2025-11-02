"""
Count Subarrays with Given XOR

Count the number of subarrays with XOR equal to given value.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


def subarrays_xor(arr: List[int], x: int) -> int:
    """
    Count subarrays with XOR equal to x using prefix XOR.
    
    If prefix_xor[i] ^ x = prefix_xor[j], then subarray from i+1 to j has XOR x.
    
    Args:
        arr: Array of integers
        x: Target XOR value
        
    Returns:
        Number of subarrays with XOR equal to x
    """
    prefix_xor_count = {}  # Map prefix XOR to count of occurrences
    prefix_xor_count[0] = 1  # Empty subarray has XOR 0
    count = 0
    current_xor = 0
    
    for num in arr:
        current_xor ^= num
        
        # If current_xor ^ x exists in map, we found subarrays with XOR x
        if current_xor ^ x in prefix_xor_count:
            count += prefix_xor_count[current_xor ^ x]
        
        # Update count of current prefix XOR
        if current_xor in prefix_xor_count:
            prefix_xor_count[current_xor] += 1
        else:
            prefix_xor_count[current_xor] = 1
    
    return count

