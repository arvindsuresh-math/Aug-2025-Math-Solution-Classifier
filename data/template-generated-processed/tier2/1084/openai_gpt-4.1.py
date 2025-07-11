def solve():
    """Index: 1084.
    Returns: the amount Billy has to pay in tips if he wants to cover 80% of a 20% tip for the two of them.
    """
    # L1
    steak_price = 20 # $20 steak
    drink_price = 5 # $5 drink
    price_per_meal = steak_price + drink_price

    # L2
    num_people = 2 # Billy and Jenny each
    total_meal_cost = price_per_meal * num_people

    # L3
    tip_percent = 0.2 # 20% tip
    total_tip = total_meal_cost * tip_percent

    # L4
    billy_tip_percent = 0.8 # 80% of the tip
    billy_tip = total_tip * billy_tip_percent

    # FA
    answer = billy_tip
    return answer