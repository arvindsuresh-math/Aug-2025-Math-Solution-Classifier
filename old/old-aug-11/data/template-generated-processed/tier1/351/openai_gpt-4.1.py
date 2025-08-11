def solve():
    """Index: 351.
    Returns: the number of peanut butter and jelly sandwiches Jackson ate for lunch this school year.
    """
    # L1
    weeks_of_school = 36 # 36 weeks of school
    sandwich_days_per_week = 2 # packs sandwich on Wednesdays and Fridays
    total_sandwich_days = weeks_of_school * sandwich_days_per_week

    # L2
    wednesdays_missed = 1 # missed 1 Wednesday
    fridays_missed = 2 # missed 2 Fridays
    total_days_missed = wednesdays_missed + fridays_missed

    # L3
    sandwiches_eaten = total_sandwich_days - total_days_missed

    # FA
    answer = sandwiches_eaten
    return answer