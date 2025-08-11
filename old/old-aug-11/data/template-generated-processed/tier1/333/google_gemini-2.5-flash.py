def solve():
    """Index: 333.
    Returns: the total number of chocolates Kantana bought for the month.
    """
    # L1
    saturdays_per_week = 1 # WK
    weeks_per_month = 4 # WK
    saturdays_in_month = saturdays_per_week * weeks_per_month

    # L2
    chocolates_for_self_per_saturday = 2 # buys 2 chocolates for herself
    chocolates_for_self_per_month = chocolates_for_self_per_saturday * saturdays_in_month

    # L3
    chocolates_for_sister_per_saturday = 1 # and 1 for her sister
    chocolates_for_sister_per_month = chocolates_for_sister_per_saturday * saturdays_in_month

    # L4
    chocolates_for_charlie = 10 # picked up an additional 10 chocolates as a birthday gift for her friend Charlie
    total_chocolates_bought = chocolates_for_charlie + chocolates_for_sister_per_month + chocolates_for_self_per_month

    # FA
    answer = total_chocolates_bought
    return answer