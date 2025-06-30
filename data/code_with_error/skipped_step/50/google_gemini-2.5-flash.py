def solve(
        monthly_spend_baseball: int = 100, # Gerald spends $100 a month on baseball supplies
        season_length_months: int = 4, # His season is 4 months long
        charge_per_chore: int = 10 # He charges $10 for each
    ):
    """Index: 50.
    Returns: the average number of chores Gerald needs to do per month to save up for his supplies.
    """

    #: L1

    #: L2
    months_not_playing_baseball = 12 - season_length_months

    #: L3
    monthly_earnings_needed = season_length_months / months_not_playing_baseball

    #: L4
    chores_per_month = monthly_earnings_needed / charge_per_chore

    #: FA
    answer = chores_per_month
    return answer