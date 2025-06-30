def solve(
    monthly_supplies_cost: int = 100, # Gerald spends $100 a month on baseball supplies
    season_length_months: int = 4, # His season is 4 months long
    total_months_in_year: int = 12, # total months in a year
    chore_charge: int = 10 # He charges $10 for each
):
    """Index: 50.
    Returns: the number of chores Gerald needs to average per month to save up for his supplies.
    """

    #: L1
    total_supplies_cost = monthly_supplies_cost * season_length_months

    #: L2
    months_to_save = total_months_in_year - season_length_months

    #: L3
    monthly_savings_needed = total_supplies_cost / months_to_save

    #: L4
    chores_per_month = monthly_savings_needed / chore_charge

    #: FA
    answer = chores_per_month
    return answer