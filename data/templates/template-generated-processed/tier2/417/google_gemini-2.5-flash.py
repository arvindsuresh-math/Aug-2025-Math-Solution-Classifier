def solve():
    """Index: 417.
    Returns: the total amount Jim paid for the car wash package.
    """
    # L1
    total_car_washes = 20 # 20 car washes
    discount_percentage_decimal = 0.6 # pay 60%
    effective_car_washes = total_car_washes * discount_percentage_decimal

    # L2
    cost_per_carwash = 15 # carwash normally costs 15 dollars
    total_cost = effective_car_washes * cost_per_carwash

    # FA
    answer = total_cost
    return answer