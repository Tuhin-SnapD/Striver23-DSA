"""
Compare Version Numbers

Compare two version numbers.

Time Complexity: O(n + m) where n and m are lengths
Space Complexity: O(1)
"""


def compare_versions(version1: str, version2: str) -> int:
    """
    Compare two version numbers.
    
    Returns: 1 if version1 > version2, -1 if version1 < version2, 0 if equal
    
    Args:
        version1: First version string
        version2: Second version string
        
    Returns:
        Comparison result: 1, -1, or 0
    """
    i = 0
    j = 0
    n = len(version1)
    m = len(version2)
    
    while i < n or j < m:
        # Extract numeric parts
        x = 0
        y = 0
        
        while i < n and version1[i] != '.':
            x = x * 10 + int(version1[i])
            i += 1
        
        while j < m and version2[j] != '.':
            y = y * 10 + int(version2[j])
            j += 1
        
        if x > y:
            return 1
        elif x < y:
            return -1
        
        # Skip dot
        i += 1
        j += 1
    
    return 0

