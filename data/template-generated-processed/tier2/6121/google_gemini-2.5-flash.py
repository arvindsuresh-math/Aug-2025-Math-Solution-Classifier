def solve():
    """Index: 6121.
    Returns: the amount of money saved by choosing the cheapest flight.
    """
    # L1
    delta_flight_cost = 850 # $850 flight with Delta Airlines
    delta_discount_percent = 0.20 # 20% discount
    delta_discount_amount = delta_flight_cost * delta_discount_percent

    # L2
    delta_final_price = delta_flight_cost - delta_discount_amount

    # L3
    united_flight_cost = 1100 # $1100 flight with United Airlines
    united_discount_percent = 0.30 # 30% off
    united_discount_amount = united_flight_cost * united_discount_percent

    # L4
    united_final_price = united_flight_cost - united_discount_amount

    # L5
    money_saved = united_final_price - delta_final_price

    # FA
    answer = money_saved
    return answer