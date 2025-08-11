def solve():
    """Index: 169.
    Returns: the total kilograms of grapes needed in a year after increasing production.
    """
    # L1
    grapes_per_6_months = 90 # 90 kilograms of grapes every 6 months
    months_per_year_factor = 2 # WK
    grapes_per_year = grapes_per_6_months * months_per_year_factor

    # L2
    increase_percent_decimal = 0.20 # increasing his production by twenty percent
    increase_amount = grapes_per_year * increase_percent_decimal

    # L3
    total_grapes_needed = grapes_per_year + increase_amount

    # FA
    answer = total_grapes_needed
    return answer