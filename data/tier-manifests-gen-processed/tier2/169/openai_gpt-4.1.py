def solve():
    """Index: 169.
    Returns: the number of kilograms of grapes Borris needs in a year after increasing production by 20%.
    """
    # L1
    grapes_per_6_months = 90 # uses 90 kilograms of grapes every 6 months
    periods_per_year = 2 # 12 months / 6 months = 2 periods per year (WK)
    grapes_per_year = grapes_per_6_months * periods_per_year

    # L2
    increase_percent = 0.20 # increasing his production by twenty percent
    increase_amount = grapes_per_year * increase_percent

    # L3
    total_grapes_needed = grapes_per_year + increase_amount

    # FA
    answer = total_grapes_needed
    return answer