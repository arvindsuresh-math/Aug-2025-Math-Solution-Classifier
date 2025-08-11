def solve():
    """Index: 206.
    Returns: the initial number of lions in Londolozi.
    """
    # L1
    cubs_born_per_month = 5 # 5 per month
    lions_die_per_month = 1 # 1 per month
    net_increase_per_month = cubs_born_per_month - lions_die_per_month

    # L2
    months_per_year = 12 # 1 year
    total_increase_per_year = net_increase_per_month * months_per_year

    # L3
    lions_after_one_year = 148 # 148 lions in Londolozi after 1 year
    initial_lions = lions_after_one_year - total_increase_per_year

    # FA
    answer = initial_lions
    return answer