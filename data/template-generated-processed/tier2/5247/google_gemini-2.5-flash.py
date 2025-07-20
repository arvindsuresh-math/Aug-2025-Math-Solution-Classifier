def solve():
    """Index: 5247.
    Returns: how much more money Juanita spends buying the newspaper yearly than Grant.
    """
    # L1
    daily_cost_weekday = 0.50 # Monday through Saturday, she spends $0.50
    weekdays_per_week = 6 # WK
    weekly_weekday_cost = weekdays_per_week * daily_cost_weekday

    # L2
    daily_cost_sunday = 2.00 # on Sunday she spends $2.00
    weekly_total_cost = daily_cost_sunday + weekly_weekday_cost

    # L3
    weeks_per_year = 52 # WK
    juanita_yearly_cost = weeks_per_year * weekly_total_cost

    # L4
    grant_yearly_cost = 200.00 # Grant spends $200.00 a year
    difference_in_cost = juanita_yearly_cost - grant_yearly_cost

    # FA
    answer = difference_in_cost
    return answer