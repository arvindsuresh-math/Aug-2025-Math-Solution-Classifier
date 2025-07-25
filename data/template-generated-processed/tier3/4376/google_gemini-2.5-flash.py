def solve():
    """Index: 4376.
    Returns: the number of weeks Austin has to work to buy the bicycle.
    """
    # L1
    hours_monday = 2 # 2 hours on Mondays
    hours_wednesday = 1 # an hour on Wednesdays
    hours_friday = 3 # 3 hours on Fridays
    total_hours_per_week = hours_monday + hours_wednesday + hours_friday

    # L2
    pay_per_hour = 5 # $5 for every hour
    earnings_per_week = pay_per_hour * total_hours_per_week

    # L3
    bicycle_cost = 180 # bicycle that costs $180
    weeks_to_work = bicycle_cost / earnings_per_week

    # FA
    answer = weeks_to_work
    return answer