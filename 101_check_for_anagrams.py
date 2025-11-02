"""
Check Permutation (Anagram)

Check if two strings are anagrams.

Time Complexity: O(n) where n is length of strings
Space Complexity: O(1) - fixed 26 characters
"""


def are_anagram(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams.
    
    Args:
        str1: First string
        str2: Second string
        
    Returns:
        True if anagrams, False otherwise
    """
    if len(str1) != len(str2):
        return False
    
    # Frequency array for 26 lowercase letters
    freq = [0] * 26
    
    # Count characters
    for i in range(len(str1)):
        freq[ord(str1[i]) - ord('a')] += 1
        freq[ord(str2[i]) - ord('a')] -= 1
    
    # Check if all frequencies are zero
    for count in freq:
        if count != 0:
            return False
    
    return True

