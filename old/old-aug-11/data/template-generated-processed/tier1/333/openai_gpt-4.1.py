def solve():
    """Index: 333.
    Returns: the total number of chocolates Kantana bought for the month.
    """
    # L1
    saturdays_per_week = 1 # 1 Saturday in a week
    weeks_per_month = 4 # 4 weeks in a month
    saturdays_per_month = saturdays_per_week * weeks_per_month

    # L2
    chocolates_for_self_per_saturday = 2 # buys 2 chocolates for herself every Saturday
    chocolates_for_self_per_month = chocolates_for_self_per_saturday * saturdays_per_month

    # L3
    chocolates_for_sister_per_saturday = 1 # buys 1 for her sister every Saturday
    chocolates_for_sister_per_month = chocolates_for_sister_per_saturday * saturdays_per_month

    # L4
    chocolates_for_charlie = 10 # picked up an additional 10 chocolates as a birthday gift for her friend Charlie
    total_chocolates = chocolates_for_charlie + chocolates_for_sister_per_month + chocolates_for_self_per_month

    # FA
    answer = total_chocolates
    return answer