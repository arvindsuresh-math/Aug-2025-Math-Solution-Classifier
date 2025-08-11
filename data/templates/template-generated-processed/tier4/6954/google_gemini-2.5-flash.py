def solve():
    """Index: 6954.
    Returns: the total amount Martin will spend on berries.
    """
    # L1
    berries_per_day_decimal = 0.5 # 1/2 cup of berries every day
    period_days = 30 # 30 day period
    total_cups_needed = berries_per_day_decimal * period_days

    # L3
    cost_per_pack = 2.00 # $2.00
    total_cost = cost_per_pack * total_cups_needed

    # FA
    answer = total_cost
    return answer