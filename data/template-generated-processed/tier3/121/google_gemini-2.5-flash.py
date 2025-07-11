def solve():
    """Index: 121.
    Returns: the total number of hours it took to fill the truck.
    """
    # L1
    rate_per_person = 250 # 250 blocks per hour per person
    initial_people = 2 # Stella and Twinkle
    initial_combined_rate = initial_people * rate_per_person

    # L2
    initial_hours_worked = 4 # four hours
    blocks_filled_initial_phase = initial_hours_worked * initial_combined_rate

    # L3
    truck_capacity = 6000 # capacity of 6000 stone blocks
    remaining_blocks = truck_capacity - blocks_filled_initial_phase

    # L4
    new_people_joined = 6 # joined by 6 other people
    total_people_second_phase = initial_people + new_people_joined

    # L5
    combined_rate_second_phase = rate_per_person * total_people_second_phase

    # L6
    hours_second_phase = remaining_blocks / combined_rate_second_phase

    # L7
    total_hours = initial_hours_worked + hours_second_phase

    # FA
    answer = total_hours
    return answer