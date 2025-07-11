def solve():
    """Index: 2985.
    Returns: the total time it will take Carly to cook all the burgers.
    """
    # L1
    total_guests = 30 # 30 guests
    half_divisor = 2 # half her 30 guests
    half_guests = total_guests / half_divisor

    # L2
    burgers_for_first_half_guests_per_person = 2 # half her 30 guests want 2 burgers
    burgers_for_first_half_guests = half_guests * burgers_for_first_half_guests_per_person

    # L3
    total_burgers = burgers_for_first_half_guests + half_guests

    # L4
    burgers_per_batch = 5 # Carly can fit 5 burgers on the grill at once
    num_batches = total_burgers / burgers_per_batch

    # L5
    cook_time_per_side = 4 # cooked for 4 minutes on each side
    num_sides = 2 # WK
    total_cook_time_per_burger = cook_time_per_side * num_sides

    # L6
    total_cook_time = total_cook_time_per_burger * num_batches

    # FA
    answer = total_cook_time
    return answer