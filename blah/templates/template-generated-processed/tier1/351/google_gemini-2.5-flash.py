def solve():
    """Index: 351.
    Returns: the total number of peanut butter and jelly sandwiches eaten.
    """
    # L1
    school_weeks = 36 # 36 weeks of school
    pbj_days_per_week = 2 # Wednesdays and Fridays
    potential_pbj_days = school_weeks * pbj_days_per_week

    # L2
    missed_wednesdays = 1 # missed 1 Wednesday
    missed_fridays = 2 # missed 2 Fridays
    total_missed_days = missed_wednesdays + missed_fridays

    # L3
    sandwiches_eaten = potential_pbj_days - total_missed_days

    # FA
    answer = sandwiches_eaten
    return answer