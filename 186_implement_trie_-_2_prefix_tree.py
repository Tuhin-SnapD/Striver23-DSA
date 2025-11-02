"""
Implement Trie (Prefix Tree)

Implement a trie data structure with insert, search, and startsWith operations.

Time Complexity:
    - Insert: O(m) where m is length of word
    - Search: O(m)
    - StartsWith: O(m)
Space Complexity: O(ALPHABET_SIZE * N * M) where N is number of words, M is avg length
"""

from typing import Optional


class TrieNode:
    """Node for trie data structure."""
    
    def __init__(self, char: str = '#'):
        self.data = char
        self.children = [None] * 26  # For 26 lowercase letters
        self.is_terminal = False  # Marks end of word


class Trie:
    """Trie (Prefix Tree) implementation."""
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """
        Insert a word into the trie.
        
        Args:
            word: Word to insert
        """
        curr = self.root
        
        for char in word:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode(char)
            curr = curr.children[index]
        
        curr.is_terminal = True
    
    def search(self, word: str) -> bool:
        """
        Search if word exists in trie.
        
        Args:
            word: Word to search
            
        Returns:
            True if word exists, False otherwise
        """
        curr = self.root
        
        for char in word:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        
        return curr.is_terminal
    
    def starts_with(self, prefix: str) -> bool:
        """
        Check if any word in trie starts with prefix.
        
        Args:
            prefix: Prefix to check
            
        Returns:
            True if prefix exists, False otherwise
        """
        curr = self.root
        
        for char in prefix:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        
        return True

