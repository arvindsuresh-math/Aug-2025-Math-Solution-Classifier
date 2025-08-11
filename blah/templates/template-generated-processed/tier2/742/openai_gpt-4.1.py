def solve():
    """Index: 742.
    Returns: the total number of yards Brendan can cut in a week after buying the lawnmower.
    """
    # L1
    base_yards_per_day = 8 # Brendan can cut 8 yards of grass per day
    percent_increase = 0.50 # Fifty percent per day
    additional_yards_per_day = base_yards_per_day * percent_increase

    # L2
    total_yards_per_day = base_yards_per_day + additional_yards_per_day

    # L3
    days_per_week = 7 # WK
    total_yards_per_week = total_yards_per_day * days_per_week

    # FA
    answer = total_yards_per_week
    return answer