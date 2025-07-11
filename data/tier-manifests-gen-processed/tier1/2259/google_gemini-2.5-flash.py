def solve():
    """Index: 2259.
    Returns: the total cost Adam would have to spend if he buys both laptops.
    """
    # L1
    first_laptop_cost = 500 # The first laptop is $500
    cost_multiplier = 3 # 3 times as costly as the first laptop
    second_laptop_cost = first_laptop_cost * cost_multiplier

    # L2
    total_cost = second_laptop_cost + first_laptop_cost

    # FA
    answer = total_cost
    return answer