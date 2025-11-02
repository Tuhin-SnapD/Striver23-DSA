"""
Maximum Profit in Job Scheduling

Schedule jobs to maximize profit with deadlines.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from typing import List

def job_scheduling(start_time: List[int], end_time: List[int], profit: List[int]) -> int:
    """
    Find maximum profit from job scheduling.
    
    Args:
        start_time: Start times of jobs
        end_time: End times of jobs
        profit: Profit from each job
        
    Returns:
        Maximum profit
    """
    # Create list of jobs with (start, end, profit)
    jobs = list(zip(start_time, end_time, profit))
    jobs.sort(key=lambda x: x[1])
    
    n = len(jobs)
    dp = [0] * n
    dp[0] = jobs[0][2]
    
    for i in range(1, n):
        # Profit without including current job
        profit_without = dp[i - 1]
        
        # Profit with including current job
        # Find last non-conflicting job using binary search
        current_profit = jobs[i][2]
        
        # Linear search for last non-conflicting job
        j = i - 1
        while j >= 0 and jobs[j][1] > jobs[i][0]:
            j -= 1
        
        if j >= 0:
            profit_with = dp[j] + current_profit
        else:
            profit_with = current_profit
        
        dp[i] = max(profit_without, profit_with)
    
    return dp[n - 1]
