def solve():
    """Index: 7251.
    Returns: the total money Melissa made from the sales.
    """
    # L1
    coupe_price = 30000 # sells a coupe for $30,000
    suv_price_multiplier = 2 # an SUV for twice as much
    suv_cost = coupe_price * suv_price_multiplier

    # L2
    total_car_cost = suv_cost + coupe_price

    # L3
    commission_rate_percent = 2 # commission is 2%
    percent_to_decimal_factor = 0.01 # WK
    earnings = total_car_cost * commission_rate_percent * percent_to_decimal_factor

    # FA
    answer = earnings
    return answer