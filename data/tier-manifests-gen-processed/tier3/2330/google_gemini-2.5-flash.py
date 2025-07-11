def solve():
    """Index: 2330.
    Returns: the total charge to paint the mural.
    """
    # L1
    mural_length = 20 # 20 ft
    mural_width = 15 # 15 ft
    mural_area = mural_length * mural_width

    # L2
    time_per_sq_ft = 20 # 20 minutes to paint 1 square foot
    total_minutes = mural_area * time_per_sq_ft

    # L3
    minutes_per_hour = 60 # WK
    total_hours = total_minutes / minutes_per_hour

    # L4
    charge_per_hour = 150 # $150 per hour
    total_charge = total_hours * charge_per_hour

    # FA
    answer = total_charge
    return answer