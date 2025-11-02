"""
Maximum XOR of Two Numbers in an Array

Find maximum XOR of any two numbers in array using Trie.

Time Complexity: O(n * 32) where 32 is number of bits
Space Complexity: O(n * 32)
"""

from typing import List, Optional


class Node:
    """Trie node for binary representation."""
    
    def __init__(self):
        """Initialize node."""
        self.links: List[Optional['Node']] = [None, None]


class Trie:
    """Binary Trie for XOR operations."""
    
    def __init__(self):
        """Initialize trie."""
        self.root = Node()
    
    def insert(self, n: int) -> None:
        """
        Insert number into trie (32-bit representation).
        
        Args:
            n: Number to insert
        """
        node = self.root
        for i in range(31, -1, -1):
            bit = (n >> i) & 1
            if node.links[bit] is None:
                node.links[bit] = Node()
            node = node.links[bit]
    
    def get_max(self, n: int) -> int:
        """
        Find maximum XOR with given number.
        
        Args:
            n: Number to find max XOR with
            
        Returns:
            Maximum XOR value
        """
        node = self.root
        ans = 0
        for i in range(31, -1, -1):
            bit = (n >> i) & 1
            # Try opposite bit to maximize XOR
            if node.links[1 - bit] is not None:
                ans |= (1 << i)
                node = node.links[1 - bit]
            else:
                node = node.links[bit]
        return ans


def maximum_xor(a: List[int]) -> int:
    """
    Find maximum XOR of any two numbers.
    
    Args:
        a: Array of integers
        
    Returns:
        Maximum XOR value
    """
    trie = Trie()
    
    # Insert all numbers
    for num in a:
        trie.insert(num)
    
    # Find maximum XOR
    ans = 0
    for num in a:
        ans = max(ans, trie.get_max(num))
    
    return ans

