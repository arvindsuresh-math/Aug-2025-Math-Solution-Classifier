def solve():
    """Index: 395.
    Returns: the rate at which new elephants entered the park (elephants/hour).
    """
    # L1
    exodus_hours = 4 # 4-hour elephant exodus
    exodus_rate = 2880 # 2,880 elephants/hour
    exodus_total = exodus_hours * exodus_rate

    # L2
    initial_elephants = 30000 # 30,000 elephants on Friday night
    elephants_after_exodus = initial_elephants - exodus_total

    # L3
    final_elephants = 28980 # final number of elephants was 28,980
    new_elephants = final_elephants - elephants_after_exodus

    # L4
    entry_hours = 7 # next 7-hour period
    entry_rate = new_elephants / entry_hours

    # FA
    answer = entry_rate
    return answer