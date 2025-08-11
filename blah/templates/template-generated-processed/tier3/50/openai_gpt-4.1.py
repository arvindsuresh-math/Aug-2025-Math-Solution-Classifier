def solve():
    """Index: 50.
    Returns: the number of chores Gerald needs to average per month to save up for his supplies.
    """
    # L1
    season_months = 4 # His season is 4 months long
    monthly_supply_cost = 100 # Gerald spends $100 a month on baseball supplies
    total_needed = season_months * monthly_supply_cost

    # L2
    months_in_year = 12 # WK
    off_season_months = months_in_year - season_months

    # L3
    monthly_savings_goal = total_needed / off_season_months

    # L4
    charge_per_chore = 10 # He charges $10 for each
    chores_per_month = monthly_savings_goal / charge_per_chore

    # FA
    answer = chores_per_month
    return answer