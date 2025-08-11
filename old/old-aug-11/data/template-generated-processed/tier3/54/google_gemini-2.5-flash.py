def solve():
    """Index: 54.
    Returns: the amount of money Leah lost.
    """
    # L1
    initial_money = 28 # Leah earned $28
    milkshake_fraction_denominator = 7 # a seventh of it
    milkshake_cost = initial_money / milkshake_fraction_denominator

    # L2
    money_after_milkshake = initial_money - milkshake_cost

    # L3
    wallet_fraction_denominator = 2 # half of the rest
    money_in_wallet = money_after_milkshake / wallet_fraction_denominator

    # L4
    remaining_after_shredding = 1 # but $1
    money_lost = money_in_wallet - remaining_after_shredding

    # FA
    answer = money_lost
    return answer