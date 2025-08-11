def solve():
    """Index: 456.
    Returns: the amount Chad will save this year.
    """
    # L1
    mowing_income = 600 # made $600 mowing yards
    birthday_income = 250.00 # received $250.00 for his birthday/holidays
    selling_income = 150.00 # made $150.00 by selling some old video games
    odd_jobs_income = 150.00 # another $150.00 doing odd jobs
    total_income = mowing_income + birthday_income + selling_income + odd_jobs_income

    # L2
    save_percent = 0.40 # saves 40% of the money
    saved_amount = total_income * save_percent

    # FA
    answer = saved_amount
    return answer