def solve():
    """Index: 5967.
    Returns: the total number of pairs of socks Laticia knitted.
    """
    # L1
    first_week_socks = 12 # In the first week, she knitted 12 pairs of socks
    second_week_increase = 4 # In the second week, she knitted 4 more pairs than the week before
    second_week_socks = first_week_socks + second_week_increase

    # L2
    first_two_weeks_total = first_week_socks + second_week_socks

    # L3
    third_week_divisor = 2 # only knitted half of the total of the first two weeks
    third_week_socks = first_two_weeks_total / third_week_divisor

    # L4
    fourth_week_decrease = 3 # In the fourth week, she knitted 3 fewer pairs than the week before
    fourth_week_socks = third_week_socks - fourth_week_decrease

    # L5
    initial_socks = 4 # Laticia knitted 4 pairs of socks for her nephew
    total_socks_knitted = initial_socks + first_week_socks + second_week_socks + third_week_socks + fourth_week_socks

    # FA
    answer = total_socks_knitted
    return answer