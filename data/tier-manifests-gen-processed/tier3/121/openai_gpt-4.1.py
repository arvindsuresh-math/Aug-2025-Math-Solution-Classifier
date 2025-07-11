def solve():
    """Index: 121.
    Returns: the total number of hours it took to fill the truck.
    """
    # L1
    rate_per_person = 250 # 250 blocks per hour per person
    initial_people = 2 # Stella and Twinkle
    initial_rate = rate_per_person * initial_people

    # L2
    initial_hours = 4 # four hours
    blocks_filled_initial = initial_hours * initial_rate

    # L3
    truck_capacity = 6000 # capacity of 6000 stone blocks
    blocks_remaining = truck_capacity - blocks_filled_initial

    # L4
    additional_people = 6 # 6 other people joined
    total_people = initial_people + additional_people

    # L5
    rate_with_all = rate_per_person * total_people

    # L6
    hours_remaining = blocks_remaining / rate_with_all

    # L7
    total_hours = initial_hours + hours_remaining

    # FA
    answer = total_hours
    return answer