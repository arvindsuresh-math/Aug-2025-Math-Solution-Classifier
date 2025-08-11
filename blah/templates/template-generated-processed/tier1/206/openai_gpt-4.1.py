def solve():
    """Index: 206.
    Returns: the number of lions in Londolozi at first.
    """
    # L1
    cubs_born_per_month = 5 # Lion cubs are born at the rate of 5 per month
    lions_die_per_month = 1 # lions die at the rate of 1 per month
    net_lions_per_month = cubs_born_per_month - lions_die_per_month

    # L2
    months_in_year = 12 # WK
    lions_added_in_year = net_lions_per_month * months_in_year

    # L3
    lions_after_year = 148 # there are 148 lions in Londolozi after 1 year
    initial_lions = lions_after_year - lions_added_in_year

    # FA
    answer = initial_lions
    return answer