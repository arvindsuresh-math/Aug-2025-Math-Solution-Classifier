def solve():
    """Index: 689.
    Returns: the total cost of the taxi ride downtown including tip.
    """
    # L1
    uber_cost = 22 # The Uber ride costs $22
    uber_vs_lyft_diff = 3 # Uber ride costs $3 more than a Lyft ride
    lyft_cost = uber_cost - uber_vs_lyft_diff

    # L2
    lyft_vs_taxi_diff = 4 # Lyft ride costs $4 more than a taxi ride
    taxi_cost = lyft_cost - lyft_vs_taxi_diff

    # L3
    tip_percent = 0.20 # tips the taxi driver 20% of the original cost
    tip_amount = taxi_cost * tip_percent

    # L4
    total_cost = taxi_cost + tip_amount

    # FA
    answer = total_cost
    return answer