def solve(
    monthly_supplies_cost: int = 100,  # Gerald spends $100 a month on baseball supplies
    season_length_months: int = 4,  # His season is 4 months long
    total_months: int = 12,  # Total months in a year
    chore_charge: int = 10  # He charges $10 for each chore
):
    """Index: 50.
    Returns: the average number of chores Gerald needs to do per month to save up for his supplies.
    """

    #: L1
    total_savings_needed = season_length_months * monthly_supplies_cost # eval: 400 = 4 * 100

    #: L2
    months_to_save = total_months - season_length_months # eval: 8 = 12 - 4

    #: L3
    monthly_savings_goal = total_savings_needed / months_to_save # eval: 50.0 = 400 / 8

    #: L4
    chores_per_month = monthly_savings_goal / chore_charge # eval: 5.0 = 50.0 / 10

    #: FA
    answer = chores_per_month
    return answer # eval: return 5.0
