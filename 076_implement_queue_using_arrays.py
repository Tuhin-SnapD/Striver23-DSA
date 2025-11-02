"""
Implement Trie II

Trie implementation with count of words and count of prefixes.

Time Complexity: O(n) where n is word length for each operation
Space Complexity: O(ALPHABET_SIZE * N * M) where N is number of words,
                  M is average word length
"""

from typing import Optional, List


class TrieNode:
    """Node for Trie with word and prefix counts."""
    
    def __init__(self):
        """Initialize trie node."""
        self.children: List[Optional['TrieNode']] = [None] * 26
        self.end_with = 0  # Count of words ending at this node
        self.count_prefix = 0  # Count of words with this prefix


class Trie:
    """Trie with word and prefix counting."""
    
    def __init__(self):
        """Initialize trie."""
        self.root = TrieNode()
    
    def _insert_word(self, root: TrieNode, word: str) -> None:
        """
        Recursively insert word into trie.
        
        Args:
            root: Current node
            word: Word to insert
        """
        if len(word) == 0:
            root.count_prefix += 1
            root.end_with += 1
            return
        
        index = ord(word[0]) - ord('a')
        
        if root.children[index] is None:
            root.children[index] = TrieNode()
        
        root.count_prefix += 1
        self._insert_word(root.children[index], word[1:])
    
    def _count_words(self, root: TrieNode, word: str) -> int:
        """
        Count occurrences of exact word.
        
        Args:
            root: Current node
            word: Word to count
            
        Returns:
            Count of word
        """
        if len(word) == 0:
            return root.end_with
        
        index = ord(word[0]) - ord('a')
        
        if root.children[index] is None:
            return 0
        
        return self._count_words(root.children[index], word[1:])
    
    def _count_word_with_prefix(self, root: TrieNode, word: str) -> int:
        """
        Count words with given prefix.
        
        Args:
            root: Current node
            word: Prefix to count
            
        Returns:
            Count of words with prefix
        """
        if len(word) == 0:
            return root.count_prefix
        
        index = ord(word[0]) - ord('a')
        
        if root.children[index] is None:
            return 0
        
        return self._count_word_with_prefix(root.children[index], word[1:])
    
    def _remove_words(self, root: TrieNode, word: str) -> None:
        """
        Remove word from trie (decrement counts).
        
        Args:
            root: Current node
            word: Word to remove
        """
        if len(word) == 0:
            root.count_prefix -= 1
            root.end_with -= 1
            return
        
        index = ord(word[0]) - ord('a')
        
        if root.children[index] is not None:
            root.count_prefix -= 1
            self._remove_words(root.children[index], word[1:])
    
    def insert(self, word: str) -> None:
        """
        Insert word into trie.
        
        Args:
            word: Word to insert
        """
        self._insert_word(self.root, word)
    
    def count_words_equal_to(self, word: str) -> int:
        """
        Count exact occurrences of word.
        
        Args:
            word: Word to count
            
        Returns:
            Count of word
        """
        return self._count_words(self.root, word)
    
    def count_words_starting_with(self, word: str) -> int:
        """
        Count words with given prefix.
        
        Args:
            word: Prefix to count
            
        Returns:
            Count of words with prefix
        """
        return self._count_word_with_prefix(self.root, word)
    
    def erase(self, word: str) -> None:
        """
        Remove word from trie.
        
        Args:
            word: Word to remove
        """
        self._remove_words(self.root, word)

