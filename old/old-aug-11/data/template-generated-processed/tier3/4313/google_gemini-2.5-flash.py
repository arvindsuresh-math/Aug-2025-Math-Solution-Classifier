def solve():
    """Index: 4313.
    Returns: the minimum number of additional weeks Bob must win first place.
    """
    # L1
    weeks_won = 2 # For the first 2 weeks
    prize_per_week = 100 # 100 dollar grand prize each time
    current_savings = weeks_won * prize_per_week

    # L2
    puppy_cost = 1000 # puppy that costs 1000 dollars
    dollars_needed = puppy_cost - current_savings

    # L3
    additional_weeks_needed = dollars_needed / prize_per_week

    # FA
    answer = additional_weeks_needed
    return answer