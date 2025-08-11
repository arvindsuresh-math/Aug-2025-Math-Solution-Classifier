def solve():
    """Index: 4416.
    Returns: the total cost Jennie paid for the car rental.
    """
    # L2
    total_rental_days = 11 # Jennie rented a car for 11 days
    days_in_week = 7 # WK
    remaining_days = total_rental_days - days_in_week

    # L3
    daily_rate = 30 # $30/day
    cost_additional_days = remaining_days * daily_rate

    # L4
    cost_first_week = 190 # $190 for the first week
    total_cost = cost_first_week + cost_additional_days

    # FA
    answer = total_cost
    return answer