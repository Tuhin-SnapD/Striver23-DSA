"""
K-th Permutation Sequence

Find kth permutation of numbers from 1 to n.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""


def kth_permutation(n: int, k: int) -> str:
    """
    Find kth permutation using factorial-based approach.
    
    Args:
        n: Number of elements (1 to n)
        k: Kth permutation (1-indexed)
        
    Returns:
        Kth permutation as string
    """
    # Build array [1, 2, ..., n]
    arr = [str(i) for i in range(1, n + 1)]
    result = ""
    
    # Calculate (n-1)!
    fact = 1
    for i in range(1, n):
        fact *= i
    
    k -= 1  # Convert to 0-indexed
    
    while True:
        # Choose element at position k/fact
        result += arr[k // fact]
        # Remove chosen element
        arr.pop(k // fact)
        
        if len(arr) == 0:
            break
        
        # Update k and fact for next iteration
        k = k % fact
        fact = fact // len(arr)
    
    return result

