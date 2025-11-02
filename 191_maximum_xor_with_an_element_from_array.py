"""
Maximum XOR With an Element From Array

For each query (xi, ai), find maximum XOR of xi with array elements <= ai.

Time Complexity: O(n log n + q log q + (n + q) * 32)
Space Complexity: O(n * 32)
"""

from typing import List, Tuple


class Node:
    """Trie node for binary representation."""
    
    def __init__(self, data: int = 0):
        """
        Initialize node.
        
        Args:
            data: Data value (not used, kept for compatibility)
        """
        self.child: List[Optional['Node']] = [None, None]


class Trie:
    """Binary Trie for XOR operations."""
    
    def __init__(self):
        """Initialize trie."""
        self.root = Node(0)
    
    def insert(self, num: int) -> None:
        """
        Insert 32-bit integer into trie.
        
        Args:
            num: Number to insert
        """
        prev = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if prev.child[bit] is None:
                prev.child[bit] = Node(bit)
            prev = prev.child[bit]
    
    def find_max(self, num: int) -> int:
        """
        Find maximum XOR with given number.
        
        Args:
            num: Number to find max XOR with
            
        Returns:
            Maximum XOR value
        """
        val = 0
        prev = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            # Try opposite bit to maximize XOR
            if bit == 1:
                if prev.child[0] is not None:
                    prev = prev.child[0]
                    val |= (1 << i)
                else:
                    prev = prev.child[1]
            else:
                if prev.child[1] is not None:
                    prev = prev.child[1]
                    val |= (1 << i)
                else:
                    prev = prev.child[0]
        return val


def max_xor_queries(arr: List[int], queries: List[List[int]]) -> List[int]:
    """
    Answer queries: max XOR of xi with array elements <= ai.
    
    Args:
        arr: Array of integers
        queries: List of [xi, ai] queries
        
    Returns:
        List of answers for each query
    """
    trie = Trie()
    
    # Sort array
    arr.sort()
    
    # Create offline queries: (ai, (xi, query_index))
    offline_queries: List[Tuple[int, Tuple[int, int]]] = []
    for i, query in enumerate(queries):
        xi, ai = query
        offline_queries.append((ai, (xi, i)))
    
    # Sort by ai (to process smaller ai first)
    offline_queries.sort()
    
    ans = [0] * len(queries)
    idx = 0
    
    # Process queries in sorted order
    for ai, (xi, q_index) in offline_queries:
        # Insert array elements <= ai into trie
        while idx < len(arr) and arr[idx] <= ai:
            trie.insert(arr[idx])
            idx += 1
        
        if idx == 0:
            # No elements inserted
            ans[q_index] = -1
        else:
            ans[q_index] = trie.find_max(xi)
    
    return ans

