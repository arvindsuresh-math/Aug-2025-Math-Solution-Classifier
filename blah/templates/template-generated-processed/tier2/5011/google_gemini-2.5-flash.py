def solve():
    """Index: 5011.
    Returns: the total cost Charlotte will spend on mani/pedis.
    """
    # L1
    regular_rate = 40.00 # mani/pedis for $40.00
    discount_rate_decimal = 0.25 # 25% off their regular rate
    discount_amount = regular_rate * discount_rate_decimal

    # L2
    cost_per_mani_pedi = regular_rate - discount_amount

    # L3
    num_people = 5 # herself, her daughter and 3 granddaughters
    total_cost = num_people * cost_per_mani_pedi

    # FA
    answer = total_cost
    return answer