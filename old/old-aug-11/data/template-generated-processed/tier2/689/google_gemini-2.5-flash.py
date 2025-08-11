def solve():
    """Index: 689.
    Returns: the total cost of the taxi ride downtown.
    """
    # L1
    uber_cost = 22 # The Uber ride costs $22
    uber_lyft_difference = 3 # costs $3 more than a Lyft ride
    lyft_cost = uber_cost - uber_lyft_difference

    # L2
    lyft_taxi_difference = 4 # costs $4 more than a taxi ride
    taxi_original_cost = lyft_cost - lyft_taxi_difference

    # L3
    tip_percentage = 0.20 # tips the taxi driver 20% of the original cost
    tip_amount = taxi_original_cost * tip_percentage

    # L4
    total_cost = taxi_original_cost + tip_amount

    # FA
    answer = total_cost
    return answer