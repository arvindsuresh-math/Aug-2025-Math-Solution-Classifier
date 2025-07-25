def solve():
    """Index: 4127.
    Returns: the number of daisies sold on the 4th day.
    """
    # L1
    daisies_day1 = 45 # sold 45 daisies on its first day
    more_day2_than_day1 = 20 # sold 20 more flowers than they did on their first day
    daisies_day2 = daisies_day1 + more_day2_than_day1

    # L2
    multiplier_twice = 2 # twice the flowers
    twice_day2 = daisies_day2 * multiplier_twice

    # L3
    less_day3_than_twice_day2 = 10 # sold 10 less than twice the flowers that were sold than on the second day
    daisies_day3 = twice_day2 - less_day3_than_twice_day2

    # L4
    total_daisies_3_days = daisies_day1 + daisies_day2 + daisies_day3

    # L5
    total_daisies_4_days = 350 # sold a total of 350 daisies for 4 days
    daisies_day4 = total_daisies_4_days - total_daisies_3_days

    # FA
    answer = daisies_day4
    return answer