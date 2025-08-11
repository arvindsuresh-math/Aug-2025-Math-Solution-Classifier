def solve():
    """Index: 4892.
    Returns: the money Liam has left after paying his bills.
    """
    # L1
    saved_per_month = 500 # $500/month
    years_saved = 2 # 2 years
    months_per_year = 12 # WK
    total_saved = (saved_per_month * months_per_year) * years_saved

    # L2
    bills_cost = 3500 # bills cost $3,500
    money_left_after_bills = total_saved - bills_cost

    # FA
    answer = money_left_after_bills
    return answer