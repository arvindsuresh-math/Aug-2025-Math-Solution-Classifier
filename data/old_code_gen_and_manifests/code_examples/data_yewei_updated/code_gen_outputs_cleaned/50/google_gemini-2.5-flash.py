def solve(
        monthly_spend_baseball: int = 100, # Gerald spends $100 a month on baseball supplies
        season_length_months: int = 4, # His season is 4 months long
        charge_per_chore: int = 10, # He charges $10 for each
        months_in_year: int = 12 # Implicit: 12 months in a year for "months he's not playing baseball"
    ):
    """Index: 50.
    Returns: the average number of chores Gerald needs to do per month to save up for his supplies.
    """
    #: L1
    total_savings_needed = season_length_months * monthly_spend_baseball

    #: L2
    months_available_for_saving = months_in_year - season_length_months

    #: L3
    monthly_earning_goal = total_savings_needed / months_available_for_saving

    #: L4
    chores_per_month_average = monthly_earning_goal / charge_per_chore

    answer = chores_per_month_average # FINAL ANSWER
    return answer