def solve():
    """Index: 3990.
    Returns: the total cost in dollars the charity spent on food.
    """
    # L1
    rice_cost_per_plate = 10 # The rice cost ten cents a plate
    chicken_cost_per_plate = 40 # the chicken cost forty cents a plate
    cost_per_plate_cents = rice_cost_per_plate + chicken_cost_per_plate

    # L2
    number_of_plates = 100 # They have a hundred plates to deliver
    total_cost_cents = cost_per_plate_cents * number_of_plates

    # L3
    cents_per_dollar = 100 # WK
    total_cost_dollars = total_cost_cents / cents_per_dollar

    # FA
    answer = total_cost_dollars
    return answer