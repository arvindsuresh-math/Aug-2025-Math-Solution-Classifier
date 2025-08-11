def solve():
    """Index: 5932.
    Returns: the amount Jenine needs to spend on more pencils.
    """
    # L1
    sharpenings_per_pencil = 5 # sharpen a pencil 5 times
    hours_per_sharpening = 1.5 # 1.5 hours of use
    pencil_lifespan_hours = sharpenings_per_pencil * hours_per_sharpening

    # L2
    initial_pencils = 10 # ten pencils
    total_initial_pencil_lifespan = initial_pencils * pencil_lifespan_hours

    # L3
    total_hours_needed = 105 # write for 105 hours
    additional_hours_needed = total_hours_needed - total_initial_pencil_lifespan

    # L4
    additional_pencils_needed = additional_hours_needed / pencil_lifespan_hours

    # L5
    cost_per_new_pencil = 2 # A new pencil costs $2
    total_cost_additional_pencils = additional_pencils_needed * cost_per_new_pencil

    # FA
    answer = total_cost_additional_pencils
    return answer