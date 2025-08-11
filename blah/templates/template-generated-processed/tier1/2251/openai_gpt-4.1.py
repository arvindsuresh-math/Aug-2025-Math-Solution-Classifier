def solve():
    """Index: 2251.
    Returns: the profit Tom earned last month.
    """
    # L1
    lawns_mowed = 3 # mows 3 lawns
    charge_per_lawn = 12 # charging $12 per lawn mowed
    mowing_income = lawns_mowed * charge_per_lawn

    # L2
    extra_weed_income = 10 # made extra money pulling weeds for $10
    total_income = mowing_income + extra_weed_income

    # L3
    gas_cost = 17 # spends $17 on gas
    profit = total_income - gas_cost

    # FA
    answer = profit
    return answer