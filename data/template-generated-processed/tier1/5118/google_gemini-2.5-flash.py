def solve():
    """Index: 5118.
    Returns: the total number of marigolds sold during the sale.
    """
    # L1
    marigolds_day1 = 14 # 14 marigolds were sold
    marigolds_day2 = 25 # 25 more marigolds were sold
    marigolds_first_two_days = marigolds_day1 + marigolds_day2

    # L2
    multiplier_third_day = 2 # two times the number
    marigolds_day3 = marigolds_day2 * multiplier_third_day

    # L3
    total_marigolds_sold = marigolds_first_two_days + marigolds_day3

    # FA
    answer = total_marigolds_sold
    return answer