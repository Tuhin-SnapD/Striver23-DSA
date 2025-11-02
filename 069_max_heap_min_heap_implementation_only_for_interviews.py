"""
Min Heap Implementation

Implement min heap operations (insert, remove).

Time Complexity: O(log n) per operation
Space Complexity: O(n)
"""

from typing import List


def min_heapify(i: int, heap: List[int]) -> None:
    """
    Heapify down from index i.
    
    Args:
        i: Index to heapify from
        heap: Heap array
    """
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    smallest = i
    
    if left_child < len(heap) and heap[left_child] < heap[i]:
        smallest = left_child
    
    if (right_child < len(heap) and
            heap[right_child] < heap[smallest]):
        smallest = right_child
    
    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        min_heapify(smallest, heap)


def insert(heap: List[int], x: int) -> None:
    """
    Insert element into min heap.
    
    Args:
        heap: Heap array
        x: Element to insert
    """
    heap.append(x)
    idx = len(heap) - 1
    parent = (idx - 1) // 2
    
    while parent >= 0 and heap[parent] > heap[idx]:
        min_heapify(parent, heap)
        idx = parent
        parent = (parent - 1) // 2


def remove_head(heap: List[int]) -> int:
    """
    Remove and return minimum element.
    
    Args:
        heap: Heap array
        
    Returns:
        Minimum element
    """
    ans = heap[0]
    heap[0], heap[-1] = heap[-1], heap[0]
    heap.pop()
    min_heapify(0, heap)
    return ans


def min_heap(n: int, q: List[List[int]]) -> List[int]:
    """
    Process min heap queries.
    
    Query format: [0, x] = insert x, [1] = remove min
    
    Args:
        n: Number of queries
        q: List of queries
        
    Returns:
        List of removed elements
    """
    heap = []
    result = []
    
    for query in q:
        if query[0] == 0:
            insert(heap, query[1])
        else:
            result.append(remove_head(heap))
    
    return result

