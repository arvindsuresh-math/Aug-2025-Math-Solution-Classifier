def solve():
    """Index: 3094.
    Returns: Gina's hourly wage.
    """
    # L1
    rose_cups_order = 6 # 6 rose cups
    rose_cups_per_hour = 6 # six cups an hour with roses
    time_for_rose_cups = rose_cups_order / rose_cups_per_hour

    # L2
    lily_cups_order = 14 # 14 lily cups
    lily_cups_per_hour = 7 # 7 cups an hour with lilies
    time_for_lily_cups = lily_cups_order / lily_cups_per_hour

    # L3
    total_painting_time = time_for_rose_cups + time_for_lily_cups

    # L4
    total_earnings = 90 # $90 total for the order
    hourly_wage = total_earnings / total_painting_time

    # FA
    answer = hourly_wage
    return answer