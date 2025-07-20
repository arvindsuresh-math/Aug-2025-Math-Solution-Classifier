def solve():
    """Index: 7174.
    Returns: the amount of cash Lulu was left with.
    """
    # L1
    initial_money = 65 # Lulu has $65 in her piggy bank
    ice_cream_cost = 5 # She spent $5 on ice cream
    money_after_ice_cream = initial_money - ice_cream_cost

    # L2
    t_shirt_divisor = 2 # spent half of the remainder
    money_after_tshirt = money_after_ice_cream / t_shirt_divisor

    # L3
    deposit_divisor = 5 # deposited a fifth of her remaining money
    deposited_money = money_after_tshirt / deposit_divisor

    # L4
    cash_left = money_after_tshirt - deposited_money

    # FA
    answer = cash_left
    return answer