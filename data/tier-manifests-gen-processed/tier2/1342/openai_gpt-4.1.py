def solve():
    """Index: 1342.
    Returns: the total amount of money James has after the windfall.
    """
    # L1
    weekly_deposit = 2000 # invests $2000 a week
    weeks_per_year = 52 # WK: number of weeks in a year
    total_deposited = weekly_deposit * weeks_per_year

    # L2
    starting_balance = 250000 # had $250,000 in his account when the year started
    end_of_year_balance = starting_balance + total_deposited

    # L3
    windfall_percent = 0.5 # windfall is worth 50% more than what he has in his bank account
    windfall_amount = windfall_percent * end_of_year_balance

    # L4
    windfall_total = windfall_amount + end_of_year_balance

    # L5
    total_money = windfall_total + end_of_year_balance

    # FA
    answer = total_money
    return answer