def solve():
    """Index: 7087.
    Returns: the number of hours Sangita must fly per month.
    """
    # L1
    day_flying_hours = 50 # 50 hours of day flying
    night_flying_hours = 9 # 9 hours of night flying
    cross_country_hours = 121 # 121 hours flying cross-country
    hours_already_flown = day_flying_hours + night_flying_hours + cross_country_hours

    # L2
    required_hours = 1500 # required to fly 1,500 hours
    remaining_hours = required_hours - hours_already_flown

    # L3
    months_to_goal = 6 # exactly 6 months
    hours_per_month = remaining_hours / months_to_goal

    # FA
    answer = hours_per_month
    return answer