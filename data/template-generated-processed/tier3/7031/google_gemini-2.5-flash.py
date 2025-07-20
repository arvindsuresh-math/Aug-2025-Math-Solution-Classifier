def solve():
    """Index: 7031.
    Returns: the amount of money Darwin had left.
    """
    # L1
    total_money = 600 # Darwin has 600$
    gas_fraction_denominator = 3 # spent 1/3 of it on gas
    cost_of_gas = total_money / gas_fraction_denominator

    # L2
    money_after_gas = total_money - cost_of_gas

    # L3
    food_fraction_denominator = 4 # 1/4 of what was left on food
    cost_of_food = money_after_gas / food_fraction_denominator

    # L4
    money_left = money_after_gas - cost_of_food

    # FA
    answer = money_left
    return answer