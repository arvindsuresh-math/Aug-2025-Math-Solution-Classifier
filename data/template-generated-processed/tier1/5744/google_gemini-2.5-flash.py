def solve():
    """Index: 5744.
    Returns: the amount of money they have left after buying passes.
    """
    # L1
    olivia_money = 112 # Olivia has $112
    nigel_money = 139 # Nigel has $139
    total_initial_money = olivia_money + nigel_money

    # L2
    num_passes = 6 # six one day passes
    cost_per_ticket = 28 # $28 per ticket
    total_passes_cost = num_passes * cost_per_ticket

    # L3
    money_left = total_initial_money - total_passes_cost

    # FA
    answer = money_left
    return answer