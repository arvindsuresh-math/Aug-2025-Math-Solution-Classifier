def solve():
    """Index: 6738.
    Returns: the number of supplemental tanks needed.
    """
    # L1
    total_dive_hours = 8 # be underwater for 8 hours
    primary_tank_hours = 2 # primary tank, which she wears when she first enters the water, has enough oxygen to allow her to stay underwater for 2 hours
    additional_hours_needed = total_dive_hours - primary_tank_hours

    # L2
    hours_per_supplemental_tank = 1 # 1-hour supplemental tanks
    num_supplemental_tanks = additional_hours_needed / hours_per_supplemental_tank

    # FA
    answer = num_supplemental_tanks
    return answer