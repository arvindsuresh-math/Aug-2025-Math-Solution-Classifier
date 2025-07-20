def solve():
    """Index: 6150.
    Returns: the final height of the tree in centimeters.
    """
    # L1
    weeks_per_month = 4 # WK
    number_of_months = 4 # in 4 months
    total_weeks = number_of_months * weeks_per_month

    # L2
    growth_rate_interval_weeks = 2 # every two weeks
    number_of_growth_intervals = total_weeks / growth_rate_interval_weeks

    # L3
    growth_per_period = 50 # fifty centimeters every two weeks
    height_increase = number_of_growth_intervals * growth_per_period

    # L4
    current_height_meters = 2 # currently 2 meters tall
    meter_unit = 1 # WK
    cm_per_meter = 100 # WK
    current_height_cm = current_height_meters * cm_per_meter

    # L5
    final_height_cm = height_increase + current_height_cm

    # FA
    answer = final_height_cm
    return answer