def solve():
    """Index: 947.
    Returns: the number of days until Johnny has 3 times as much practice as he does currently.
    """
    # L1
    days_ago = 20 # as of 20 days ago
    half = 2 # had half as much practice
    current_days_practiced = days_ago * half

    # L2
    triple = 3 # three times as much practice
    needed_total_days = current_days_practiced * triple

    # L3
    more_days_needed = needed_total_days - current_days_practiced

    # FA
    answer = more_days_needed
    return answer