def solve():
    """Index: 5455.
    Returns: the number of chocolates remaining uneaten on the fifth day.
    """
    # L1
    chocolates_day1 = 4 # ate 4 chocolates
    multiplier_twice = 2 # twice as many chocolates
    twice_day1 = multiplier_twice * chocolates_day1

    # L2
    less_than_twice = 3 # 3 less than twice as many chocolates
    chocolates_day2 = twice_day1 - less_than_twice

    # L3
    less_than_day1_day3 = 2 # two less than the number she ate on the first day
    chocolates_day3 = chocolates_day1 - less_than_day1_day3

    # L4
    less_than_day3_day4 = 1 # one less than she ate the previous day
    chocolates_day4 = chocolates_day3 - less_than_day3_day4

    # L5
    total_eaten = chocolates_day1 + chocolates_day2 + chocolates_day3 + chocolates_day4

    # L6
    initial_chocolates = 24 # box of 24 chocolates
    remaining_chocolates = initial_chocolates - total_eaten

    # FA
    answer = remaining_chocolates
    return answer