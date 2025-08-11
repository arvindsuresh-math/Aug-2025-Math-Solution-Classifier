def solve():
    """Index: 2251.
    Returns: the total profit Tom earned last month.
    """
    # L1
    num_lawns_mowed = 3 # mows 3 lawns
    charge_per_lawn = 12 # charging $12 per lawn mowed
    earnings_from_lawns = num_lawns_mowed * charge_per_lawn

    # L2
    extra_money_weeds = 10 # made extra money pulling weeds for $10
    total_earnings = earnings_from_lawns + extra_money_weeds

    # L3
    gas_cost_per_month = 17 # spends $17 on gas
    profit = total_earnings - gas_cost_per_month

    # FA
    answer = profit
    return answer