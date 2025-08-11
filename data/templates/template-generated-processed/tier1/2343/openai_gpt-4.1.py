def solve():
    """Index: 2343.
    Returns: the number of toy cars Jerome had originally.
    """
    # L1
    last_month_bought = 5 # Jerome bought 5 new toy cars last month
    times_more_this_month = 2 # bought twice as many this month
    this_month_bought = last_month_bought * times_more_this_month

    # L2
    total_bought = last_month_bought + this_month_bought

    # L3
    total_now = 40 # he has 40 toy cars now
    originally_had = total_now - total_bought

    # FA
    answer = originally_had
    return answer