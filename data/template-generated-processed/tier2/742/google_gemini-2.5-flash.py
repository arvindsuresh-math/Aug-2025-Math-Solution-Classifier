def solve():
    """Index: 742.
    Returns: the total number of yards Brendan can cut in a week.
    """
    # L1
    initial_yards_per_day = 8 # cut 8 yards of grass per day
    increase_percent_decimal = 0.50 # Fifty percent per day
    additional_yards_per_day = initial_yards_per_day * increase_percent_decimal

    # L2
    total_yards_per_day_with_mower = initial_yards_per_day + additional_yards_per_day

    # L3
    days_per_week = 7 # after a week
    total_yards_per_week = total_yards_per_day_with_mower * days_per_week

    # FA
    answer = total_yards_per_week
    return answer