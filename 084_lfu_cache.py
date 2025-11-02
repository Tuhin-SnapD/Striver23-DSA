"""
LFU Cache Implementation

Least Frequently Used cache with get and put operations.

Time Complexity: O(1) for both get and put
Space Complexity: O(capacity)
"""

from typing import Dict, List, Optional


class LFUCache:
    """LFU Cache implementation."""
    
    def __init__(self, capacity: int):
        """
        Initialize LFU cache.
        
        Args:
            capacity: Maximum capacity of cache
        """
        self.capacity = capacity
        self.min_freq = 0
        # Cache: key -> (value, frequency)
        self.cache: Dict[int, tuple] = {}
        # Frequency map: frequency -> list of keys
        self.freq_map: Dict[int, List[int]] = {}
        # Position map: key -> index in freq_map
        self.pos: Dict[int, int] = {}
    
    def get(self, key: int) -> int:
        """
        Get value for key, incrementing its frequency.
        
        Args:
            key: Key to look up
            
        Returns:
            Value if exists, -1 otherwise
        """
        if key in self.cache:
            value, freq = self.cache[key]
            # Remove from current frequency list
            self.freq_map[freq].remove(key)
            
            freq += 1
            
            # Add to new frequency list
            if freq not in self.freq_map:
                self.freq_map[freq] = []
            self.freq_map[freq].insert(0, key)
            self.pos[key] = 0
            
            # Update min_freq if needed
            if not self.freq_map[self.min_freq]:
                self.min_freq += 1
            
            # Update cache
            self.cache[key] = (value, freq)
            return value
        
        return -1
    
    def put(self, key: int, value: int) -> None:
        """
        Insert or update key-value pair.
        
        Args:
            key: Key
            value: Value
        """
        if key in self.cache:
            # Update existing
            _, freq = self.cache[key]
            self.freq_map[freq].remove(key)
            
            freq += 1
            if freq not in self.freq_map:
                self.freq_map[freq] = []
            self.freq_map[freq].insert(0, key)
            self.pos[key] = 0
            
            if not self.freq_map[self.min_freq]:
                self.min_freq += 1
            
            self.cache[key] = (value, freq)
            return
        
        # Insert new
        if len(self.cache) == self.capacity:
            # Remove LFU element
            lfu_key = self.freq_map[self.min_freq].pop()
            del self.cache[lfu_key]
            del self.pos[lfu_key]
        
        # Add new element
        self.cache[key] = (value, 1)
        if 1 not in self.freq_map:
            self.freq_map[1] = []
        self.freq_map[1].insert(0, key)
        self.pos[key] = 0
        self.min_freq = 1

