def solve():
    """Index: 50.
    Returns: the average number of chores needed per month to save for supplies.
    """
    # L1
    season_length_months = 4 # His season is 4 months long
    monthly_expense = 100 # spends $100 a month
    total_supplies_cost = season_length_months * monthly_expense

    # L2
    months_per_year = 12 # WK
    months_to_save = months_per_year - season_length_months

    # L3
    monthly_earning_goal = total_supplies_cost / months_to_save

    # L4
    charge_per_chore = 10 # He charges $10 for each
    chores_per_month = monthly_earning_goal / charge_per_chore

    # FA
    answer = chores_per_month
    return answer