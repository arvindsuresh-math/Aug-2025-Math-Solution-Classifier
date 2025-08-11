def solve():
    """Index: 6146.
    Returns: the amount of money left after buying the gift and cake.
    """
    # L1
    gift_cost = 250 # gift that costs $250
    half_divisor = 2 # half of the cost of the gift
    rick_savings = gift_cost / half_divisor

    # L2
    erika_savings = 155 # Erika saved $155
    total_savings = erika_savings + rick_savings

    # L3
    cake_cost = 25 # a birthday cake that costs $25
    total_cost = gift_cost + cake_cost

    # L4
    money_left = total_savings - total_cost

    # FA
    answer = money_left
    return answer