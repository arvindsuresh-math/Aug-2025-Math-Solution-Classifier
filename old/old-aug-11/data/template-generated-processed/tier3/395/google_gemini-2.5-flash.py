def solve():
    """Index: 395.
    Returns: the rate at which new elephants entered the park.
    """
    # L1
    exodus_duration_hours = 4 # a 4-hour elephant exodus
    exodus_rate_per_hour = 2880 # at a constant rate of 2,880 elephants/hour
    exodus_total_elephants = exodus_duration_hours * exodus_rate_per_hour

    # L2
    initial_elephants = 30000 # hosted 30,000 elephants on Friday night
    elephants_after_exodus = initial_elephants - exodus_total_elephants

    # L3
    final_elephants = 28980 # final number of elephants in the park was 28,980
    new_elephants_entered = final_elephants - elephants_after_exodus

    # L4
    entry_duration_hours = 7 # Over the next 7-hour period
    entry_rate_per_hour = new_elephants_entered / entry_duration_hours

    # FA
    answer = entry_rate_per_hour
    return answer