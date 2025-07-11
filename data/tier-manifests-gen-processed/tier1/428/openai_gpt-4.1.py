def solve():
    """Index: 428.
    Returns: the total number of eggs the frog laid over 4 days.
    """
    # L1
    day1_eggs = 50 # first day she lays 50 eggs

    # L2
    day2_multiplier = 2 # she doubles her production of eggs
    day2_eggs = day1_eggs * day2_multiplier

    # L3
    day3_extra = 20 # third day she lays 20 more than the second day
    day3_eggs = day2_eggs + day3_extra

    # L4
    day4_multiplier = 2 # she doubles the first three days total
    day4_eggs = day4_multiplier * (day1_eggs + day2_eggs + day3_eggs)

    # L5
    total_eggs = day1_eggs + day2_eggs + day3_eggs + day4_eggs

    # FA
    answer = total_eggs
    return answer