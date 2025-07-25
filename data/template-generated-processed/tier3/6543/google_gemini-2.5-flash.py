def solve():
    """Index: 6543.
    Returns: the number of days the astronaut will spend on Orbius-5.
    """
    # L1
    days_per_year = 250 # 250 days per year
    seasons_per_year = 5 # 5 seasons
    days_per_season = days_per_year / seasons_per_year

    # L2
    seasons_stayed = 3 # stays there for 3 seasons
    total_days_stayed = seasons_stayed * days_per_season

    # FA
    answer = total_days_stayed
    return answer