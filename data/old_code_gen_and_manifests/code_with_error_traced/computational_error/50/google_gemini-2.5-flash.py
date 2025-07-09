def solve(
        monthly_spend_baseball: int = 100, # Gerald spends $100 a month on baseball supplies
        season_length_months: int = 4, # His season is 4 months long
        charge_per_chore: int = 10 # He charges $10 for each
    ):
    """Index: 50.
    Returns: the average number of chores Gerald needs to do per month to save up for his supplies.
    """

    #: L1
    total_savings_needed = season_length_months * monthly_spend_baseball # eval: 400 = 4 * 100

    #: L2
    months_not_playing_baseball = -2 # eval: -2 = -2

    #: L3
    monthly_earnings_needed = total_savings_needed / months_not_playing_baseball # eval: -200.0 = 400 / -2

    #: L4
    chores_per_month = monthly_earnings_needed / charge_per_chore # eval: -20.0 = -200.0 / 10

    #: FA
    answer = chores_per_month
    return answer # eval: return -20.0
