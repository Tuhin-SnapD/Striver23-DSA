"""
Modular Exponentiation

Calculate (x^n) % m efficiently using binary exponentiation.

Time Complexity: O(log n)
Space Complexity: O(1)
"""


def modular_exponentiation(x: int, n: int, m: int) -> int:
    """
    Calculate (x^n) % m using binary exponentiation (fast exponentiation).
    
    Args:
        x: Base
        n: Exponent
        m: Modulus
        
    Returns:
        Result of (x^n) % m
    """
    ans = 1
    xx = x % m
    
    while n > 0:
        # If n is odd, multiply answer by current base
        if n % 2 != 0:
            ans = (ans % m * xx % m) % m
        
        # Square the base
        xx = (xx % m * xx % m) % m
        
        # Divide exponent by 2
        n = n >> 1
    
    return int(ans % m)

