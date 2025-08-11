def solve():
    """Index: 5185.
    Returns: the total number of swordfish caught by Shelly and Sam.
    """
    # L1
    shelly_five_swordfish = 5 # five swordfish
    shelly_less_than_five = 2 # 2 less
    shelly_per_trip = shelly_five_swordfish - shelly_less_than_five

    # L2
    sam_less_than_shelly = 1 # one less swordfish than Shelly
    sam_per_trip = shelly_per_trip - sam_less_than_shelly

    # L3
    total_per_trip = shelly_per_trip + sam_per_trip

    # L4
    num_trips = 5 # go fishing 5 times
    total_swordfish = total_per_trip * num_trips

    # FA
    answer = total_swordfish
    return answer