def solve():
    """Index: 208.
    Returns: the number of dollars left in John's piggy bank after the car repair.
    """
    # L1
    months_per_year = 12 # WK
    years_saving = 2 # 2 years
    total_months = months_per_year * years_saving

    # L2
    monthly_saving = 25 # $25 in his piggy bank every month
    total_saved = monthly_saving * total_months

    # L3
    amount_spent = 400 # spent $400 from his piggy bank savings
    remaining = total_saved - amount_spent

    # FA
    answer = remaining
    return answer