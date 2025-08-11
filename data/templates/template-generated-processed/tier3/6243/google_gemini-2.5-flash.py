def solve():
    """Index: 6243.
    Returns: the total money Jebb spent at the restaurant.
    """
    # L1
    food_cost = 50 # $50 worth of food
    service_fee_percentage = 12 # service fee of 12%
    percentage_divisor = 100 # WK
    service_fee = food_cost * service_fee_percentage / percentage_divisor

    # L2
    cost_with_fee = food_cost + service_fee

    # L3
    tip_amount = 5 # gives a $5 tip
    total_cost = cost_with_fee + tip_amount

    # FA
    answer = total_cost
    return answer