def solve():
    """Index: 54.
    Returns: the amount of money Leah lost.
    """
    # L1
    initial_earnings = 28 # Leah earned $28
    milkshake_denominator = 7 # spent a seventh of it
    milkshake_cost = initial_earnings / milkshake_denominator

    # L2
    money_after_milkshake = initial_earnings - milkshake_cost

    # L3
    savings_denominator = 2 # put half of the rest
    money_in_wallet = money_after_milkshake / savings_denominator

    # L4
    money_left_intact = 1 # shredded all the money inside but $1
    money_lost = money_in_wallet - money_left_intact

    # FA
    answer = money_lost
    return answer