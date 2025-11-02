"""
Allocate Minimum Number of Pages

Given number of pages in n books, allocate to m students such that maximum
pages allocated to any student is minimized.

Time Complexity: O(n * log(sum of pages))
Space Complexity: O(1)
"""

from typing import List


def is_possible(arr: List[int], n: int, m: int, mid: int) -> bool:
    """
    Check if allocation with maximum mid pages per student is possible.
    
    Args:
        arr: Array of pages in each book
        n: Number of books
        m: Number of students
        mid: Maximum pages allowed per student
        
    Returns:
        True if allocation is possible, False otherwise
    """
    student_count = 1
    page_sum = 0
    
    for i in range(n):
        if page_sum + arr[i] <= mid:
            page_sum += arr[i]
        else:
            student_count += 1
            if student_count > m or arr[i] > mid:
                return False
            page_sum = arr[i]
    
    return True


def allocate_books(arr: List[int], n: int, m: int) -> int:
    """
    Find minimum maximum pages allocated to any student.
    
    Uses binary search on the answer.
    
    Args:
        arr: Array of pages in each book
        n: Number of books
        m: Number of students
        
    Returns:
        Minimum maximum pages allocated, or -1 if impossible
    """
    if m > n:
        return -1
    
    start = 0
    end = sum(arr)
    ans = -1
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if is_possible(arr, n, m, mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return ans

