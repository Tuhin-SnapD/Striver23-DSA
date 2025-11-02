"""
Pow(x, n)

Compute x raised to the power n (x^n).

Time Complexity: O(log n)
Space Complexity: O(log n)
"""

def my_pow(x: float, n: int) -> float:
    """
    Compute x raised to the power n.
    
    Args:
        x: Base number
        n: Exponent (can be negative)
        
    Returns:
        x raised to the power n
    """
    # Handle negative exponent
    if n < 0:
        x = 1 / x
        n = -n
    
    # Base case
    if n == 0:
        return 1
    
    # Recursive approach: x^n = (x^(n/2))^2 if n is even
    half_pow = my_pow(x, n // 2)
    
    if n % 2 == 0:
        return half_pow * half_pow
    else:
        return x * half_pow * half_pow
