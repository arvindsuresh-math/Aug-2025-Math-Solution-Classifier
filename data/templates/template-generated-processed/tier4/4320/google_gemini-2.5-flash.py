def solve():
    """Index: 4320.
    Returns: the total cost of the mural.
    """
    # L1
    mural_length = 6 # 6m by 3m
    mural_width = 3 # 6m by 3m
    mural_area = mural_length * mural_width

    # L2
    paint_cost_per_sq_meter = 4 # $4 per square meter
    total_paint_cost = mural_area * paint_cost_per_sq_meter

    # L3
    paint_rate_sq_meter_per_hour = 1.5 # 1.5 square meters per hour
    hours_worked = mural_area / paint_rate_sq_meter_per_hour

    # L4
    artist_charge_per_hour = 10 # charges $10 per hour
    artist_labor_cost = hours_worked * artist_charge_per_hour

    # L5
    total_mural_cost = artist_labor_cost + total_paint_cost

    # FA
    answer = total_mural_cost
    return answer