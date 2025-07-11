def solve():
    """Index: 2451.
    Returns: the number of days Sanya needs to wash all towels.
    """
    # L1
    towels_per_wash = 7 # wash 7 bath towels
    hours_per_day = 2 # 2 hours in a day
    towels_per_day = towels_per_wash * hours_per_day

    # L2
    total_towels = 98 # 98 bath towels
    days_needed = total_towels / towels_per_day

    # FA
    answer = days_needed
    return answer