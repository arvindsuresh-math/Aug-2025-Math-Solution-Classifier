def solve():
    """Index: 991.
    Returns: the total number of flowers that bloom because of the trip.
    """
    # L1
    journey_km = 9 # a journey of 9 kilometers
    meters_per_kilometer = 1000 # WK
    journey_meters = journey_km * meters_per_kilometer

    # L2
    meters_per_step = 3 # each unicorn moves 3 meters forward with each step
    total_steps = journey_meters / meters_per_step

    # L3
    flowers_per_step = 4 # four flowers spring into bloom
    flowers_per_unicorn = total_steps * flowers_per_step

    # L4
    num_unicorns = 6 # six unicorns
    total_flowers = flowers_per_unicorn * num_unicorns

    # FA
    answer = total_flowers
    return answer