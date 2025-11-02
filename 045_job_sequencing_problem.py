"""
Job Sequencing Problem

Schedule jobs to maximize profit with deadline constraints.

Time Complexity: O(n^2) where n is max deadline
Space Complexity: O(n)
"""

from typing import List


def job_scheduling(jobs: List[List[int]]) -> int:
    """
    Find maximum profit by scheduling jobs within deadlines.
    
    Jobs are in format [deadline, profit].
    Uses greedy approach: schedule highest profit jobs as late as possible.
    
    Args:
        jobs: List of jobs [deadline, profit]
        
    Returns:
        Maximum profit achievable
    """
    n = len(jobs)
    
    # Sort jobs by profit (descending)
    jobs.sort(key=lambda x: x[1], reverse=True)
    
    # Find maximum deadline
    max_deadline = max(job[0] for job in jobs)
    
    # Initialize slot array
    slot = [-1] * (max_deadline + 1)
    
    job_profit = 0
    
    # Schedule each job as late as possible
    for i in range(n):
        deadline = jobs[i][0]
        profit = jobs[i][1]
        
        # Find latest available slot before deadline
        for j in range(deadline, 0, -1):
            if slot[j] == -1:
                slot[j] = i
                job_profit += profit
                break
    
    return job_profit

