def solve():
    """Index: 13.
    Returns: the total amount Jasper spent on ingredients.
    """
    # L1
    cheddar_price = 10 # 2 pounds of cheddar cheese for $10
    half_price_divisor = 2 # half the price
    cream_cheese_cost = cheddar_price / half_price_divisor

    # L2
    twice_price_multiplier = 2 # twice the price
    cold_cuts_cost = cheddar_price * twice_price_multiplier

    # L3
    total_cost = cheddar_price + cream_cheese_cost + cold_cuts_cost

    # FA
    answer = total_cost
    return answer