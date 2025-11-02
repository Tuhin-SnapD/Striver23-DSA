"""
Complete String

Find longest complete string where all prefixes exist in dictionary.

Time Complexity: O(n * m) where n is number of words, m is max word length
Space Complexity: O(ALPHABET_SIZE * N * M)
"""

from typing import List, Optional


class Node:
    """Trie node."""
    
    def __init__(self):
        """Initialize node."""
        self.arr: List[Optional['Node']] = [None] * 26
        self.flag = False  # True if word ends here


def get_node() -> Node:
    """Create and return new node."""
    node = Node()
    node.flag = False
    for i in range(26):
        node.arr[i] = None
    return node


def insert(root: Node, word: str) -> None:
    """
    Insert word into trie.
    
    Args:
        root: Root of trie
        word: Word to insert
    """
    node = root
    for char in word:
        index = ord(char) - ord('a')
        if node.arr[index] is None:
            node.arr[index] = get_node()
        node = node.arr[index]
    node.flag = True


def check(root: Node, word: str, result: List[str]) -> None:
    """
    Check if word is complete (all prefixes exist) and update result.
    
    Args:
        root: Root of trie
        word: Word to check
        result: List to store result (single element for reference)
    """
    node = root
    for char in word:
        node = node.arr[ord(char) - ord('a')]
        if not node.flag:
            return
    
    # Update result if current word is longer or lexicographically smaller
    if len(word) > len(result[0]):
        result[0] = word
    elif len(word) == len(result[0]) and word < result[0]:
        result[0] = word


def complete_string(n: int, a: List[str]) -> str:
    """
    Find longest complete string.
    
    Args:
        n: Number of strings
        a: List of strings
        
    Returns:
        Longest complete string, or "None" if no complete string exists
    """
    root = get_node()
    
    # Insert all words
    for word in a:
        insert(root, word)
    
    result = [""]
    
    # Check each word
    for word in a:
        check(root, word, result)
    
    return result[0] if result[0] else "None"

