def solve():
    """Index: 2245.
    Returns: the total number of lions in Londolozi after 1 year.
    """
    # L1
    lion_cubs_born_per_month = 5 # 5 per month
    lions_die_per_month = 1 # 1 per month
    net_increase_per_month = lion_cubs_born_per_month - lions_die_per_month

    # L2
    months_per_year = 12 # WK
    total_increase_per_year = net_increase_per_month * months_per_year

    # L3
    initial_lions = 100 # 100 lions in Londolozi at first
    final_lions = initial_lions + total_increase_per_year

    # FA
    answer = final_lions
    return answer