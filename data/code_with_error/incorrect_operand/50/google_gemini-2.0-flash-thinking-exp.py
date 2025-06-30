def solve(
    monthly_cost_supplies: int = 100, # Gerald spends $100 a month on baseball supplies
    season_length_months: int = 4, # His season is 4 months long
    charge_per_chore: int = 10, # He charges $10 for each
    total_months_in_year: int = 12 # Implied: a year has 12 months
):
    """Index: 50.
    Returns: the average number of chores Gerald needs to do per month to save for his supplies.
    """

    #: L1
    total_cost_for_season = season_length_months * monthly_cost_supplies

    #: L2
    saving_months = total_months_in_year - season_length_months

    #: L3
    monthly_saving_goal = total_cost_for_season / saving_months

    #: L4
    chores_per_month = monthly_saving_goal / total_cost_for_season

    #: FA
    answer = chores_per_month
    return answer