def solve():
    """Index: 4802.
    Returns: the number of times Mary needs to charge her vacuum cleaner.
    """
    # L1
    num_bedrooms = 3 # three bedrooms
    num_kitchens = 1 # a kitchen
    num_living_rooms = 1 # and a living room
    total_rooms = num_bedrooms + num_kitchens + num_living_rooms

    # L2
    minutes_per_room = 4 # takes her four minutes to vacuum each room
    total_vacuuming_time = minutes_per_room * total_rooms

    # L3
    charge_duration_minutes = 10 # battery charge in Mary
    num_charges_needed = total_vacuuming_time / charge_duration_minutes

    # FA
    answer = num_charges_needed
    return answer