def solve():
    """Index: 5115.
    Returns: the number of weeks needed to purchase the car.
    """
    # L1
    normal_hourly_rate = 20 # $20 per hour
    normal_hours_per_week = 40 # 40 hours per week
    normal_weekly_earnings = normal_hourly_rate * normal_hours_per_week

    # L2
    overtime_rate_multiplier = 1.5 # 1.5 times the normal rate
    overtime_hourly_rate = normal_hourly_rate * overtime_rate_multiplier

    # L3
    total_hours_per_week = 52 # 52 hours per week
    overtime_hours_per_week = total_hours_per_week - normal_hours_per_week

    # L4
    overtime_weekly_earnings = overtime_hours_per_week * overtime_hourly_rate

    # L5
    total_weekly_earnings = normal_weekly_earnings + overtime_weekly_earnings

    # L6
    car_cost = 4640 # $4640 car
    weeks_to_work = car_cost / total_weekly_earnings

    # FA
    answer = weeks_to_work
    return answer