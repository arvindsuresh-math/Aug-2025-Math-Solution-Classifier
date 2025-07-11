def solve():
    """Index: 428.
    Returns: the total number of eggs laid by the frog over 4 days.
    """
    # L1
    eggs_day1 = 50 # The first day she lays 50 eggs.

    # L2
    multiplier_double = 2 # she doubles her production of eggs
    eggs_day2 = eggs_day1 * multiplier_double

    # L3
    more_than_day2 = 20 # lays 20 more than the second day
    eggs_day3 = eggs_day2 + more_than_day2

    # L4
    multiplier_double_total = 2 # doubles the first three days total
    eggs_day4 = multiplier_double_total * (eggs_day1 + eggs_day2 + eggs_day3)

    # L5
    total_eggs = eggs_day1 + eggs_day2 + eggs_day3 + eggs_day4

    # FA
    answer = total_eggs
    return answer