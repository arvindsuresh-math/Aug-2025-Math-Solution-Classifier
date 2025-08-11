def solve():
    """Index: 1342.
    Returns: the total amount of money James has.
    """
    # L1
    weekly_investment = 2000 # invests $2000 a week
    weeks_in_year = 52 # WK
    total_weekly_deposits = weekly_investment * weeks_in_year

    # L2
    initial_account_balance = 250000 # $250,000 in his account when the year started
    balance_before_windfall = initial_account_balance + total_weekly_deposits

    # L3
    windfall_percentage_decimal = 0.5 # worth 50% more
    windfall_additional_amount = windfall_percentage_decimal * balance_before_windfall

    # L4
    account_value_after_windfall_calculation = windfall_additional_amount + balance_before_windfall

    # L5
    final_money_total = account_value_after_windfall_calculation + balance_before_windfall

    # FA
    answer = final_money_total
    return answer