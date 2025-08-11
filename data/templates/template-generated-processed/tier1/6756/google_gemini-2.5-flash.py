def solve():
    """Index: 6756.
    Returns: the total worth of the presents John gave to his fiancee.
    """
    # L1
    ring_cost = 4000 # $4000 ring
    car_cost = 2000 # $2000 car
    initial_presents_cost = ring_cost + car_cost

    # L2
    multiplier_brace = 2 # twice as expensive
    brace_cost = multiplier_brace * ring_cost

    # L3
    total_worth = initial_presents_cost + brace_cost

    # FA
    answer = total_worth
    return answer