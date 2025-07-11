def solve():
    """Index: 1643.
    Returns: the amount of money Valerie will have left over after buying the bulbs.
    """
    # L1
    num_small_bulbs = 3 # needs 3 small light bulbs
    cost_small_bulb = 8 # small light bulbs cost $8
    small_bulbs_total = num_small_bulbs * cost_small_bulb

    # L2
    cost_large_bulb = 12 # large light bulbs cost $12
    total_spent = small_bulbs_total + cost_large_bulb

    # L3
    valerie_money = 60 # She has $60 to spend
    money_left = valerie_money - total_spent

    # FA
    answer = money_left
    return answer