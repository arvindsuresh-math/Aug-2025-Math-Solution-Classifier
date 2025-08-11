def solve():
    """Index: 6960.
    Returns: the total charge for planting the flowers.
    """
    # L1
    mowing_time = 1 # 1 hour
    planting_time = 2 # planting the flowers takes 2 hours
    total_hours_worked = mowing_time + planting_time

    # L2
    desired_hourly_rate = 20 # $20/hour
    total_desired_earnings = desired_hourly_rate * total_hours_worked

    # L3
    mowing_pay = 15 # pays $15
    planting_charge = total_desired_earnings - mowing_pay

    # FA
    answer = planting_charge
    return answer