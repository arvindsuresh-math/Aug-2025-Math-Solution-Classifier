def solve():
    """Index: 736.
    Returns: the total cost of the meal including tip.
    """
    # L1
    num_samosas = 3 # three samosas
    cost_per_samosa = 2 # $2 each
    samosas_cost = num_samosas * cost_per_samosa

    # L2
    num_pakoras = 4 # four orders of pakoras
    cost_per_pakora = 3 # $3 each
    pakoras_cost = num_pakoras * cost_per_pakora

    # L3
    mango_lassi_cost = 2 # a mango lassi, for $2
    food_subtotal = samosas_cost + pakoras_cost + mango_lassi_cost

    # L4
    tip_percent = 0.25 # 25% tip
    tip_amount = food_subtotal * tip_percent

    # L5
    total_cost = food_subtotal + tip_amount

    # FA
    answer = total_cost
    return answer