def solve():
    """Index: 1084.
    Returns: the amount Billy will have to pay in tips.
    """
    # L1
    steak_price = 20 # a $20 steak
    drink_price = 5 # a $5 drink
    cost_per_meal = steak_price + drink_price

    # L2
    num_people = 2 # for the two of them
    total_cost_meals = cost_per_meal * num_people

    # L3
    tip_percent_decimal = 0.2 # a 20% tip
    total_tip_amount = total_cost_meals * tip_percent_decimal

    # L4
    billy_tip_percent_decimal = 0.8 # 80% of a 20% tip
    billy_contribution = total_tip_amount * billy_tip_percent_decimal

    # FA
    answer = billy_contribution
    return answer