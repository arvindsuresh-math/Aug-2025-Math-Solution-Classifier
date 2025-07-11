def solve():
    """Index: 2637.
    Returns: the total number of weeks to complete the dresses.
    """
    # L1
    hours_per_dress = 12 # She can sew one dress in 12 hours
    num_bridesmaids = 5 # There are 5 bridesmaids in the wedding
    total_hours_needed = hours_per_dress * num_bridesmaids

    # L2
    hours_per_week = 4 # Sheena sews the dresses 4 hours each week
    total_weeks = total_hours_needed / hours_per_week

    # FA
    answer = total_weeks
    return answer