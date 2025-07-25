def solve():
    """Index: 4577.
    Returns: the total number of milkshakes made.
    """
    # L1
    augustus_rate = 3 # 3 milkshakes per hour
    luna_rate = 7 # 7 milkshakes per hour
    combined_rate = augustus_rate + luna_rate

    # L2
    hours_worked = 8 # 8 hours now
    total_milkshakes = combined_rate * hours_worked

    # FA
    answer = total_milkshakes
    return answer