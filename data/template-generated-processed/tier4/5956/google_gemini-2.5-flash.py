def solve():
    """Index: 5956.
    Returns: the amount saved by choosing the first option.
    """
    # L1
    distance_one_way = 150 # 150 kilometers long each way
    round_trip_factor = 2 # WK
    total_distance = distance_one_way * round_trip_factor

    # L2
    kilometers_per_liter = 15 # A liter of gasoline can cover 15 kilometers
    gasoline_needed_liters = total_distance / kilometers_per_liter

    # L3
    cost_per_liter = 0.90 # costs $0.90 per liter
    total_gasoline_cost = cost_per_liter * gasoline_needed_liters

    # L4
    option1_rental_cost = 50 # The first option for a car rental costs $50 a day
    total_cost_option1 = option1_rental_cost + total_gasoline_cost

    # L5
    option2_total_cost = 90 # The second option costs $90 a day including gasoline
    savings = option2_total_cost - total_cost_option1

    # FA
    answer = savings
    return answer