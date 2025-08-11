def solve():
    """Index: 456.
    Returns: the amount Chad will save.
    """
    # L1
    mowing_yards_income = 600.00 # made $600 mowing yards
    birthday_income = 250.00 # received $250.00 for his birthday/holidays
    selling_games_income = 150.00 # made $150.00 by selling some old video games
    odd_jobs_income = 150.00 # another $150.00 doing odd jobs
    total_income = mowing_yards_income + birthday_income + selling_games_income + odd_jobs_income

    # L2
    savings_percent_text = 40 # saves 40%
    savings_percent_decimal = 0.40 # saves 40%
    amount_saved = total_income * savings_percent_decimal

    # FA
    answer = amount_saved
    return answer