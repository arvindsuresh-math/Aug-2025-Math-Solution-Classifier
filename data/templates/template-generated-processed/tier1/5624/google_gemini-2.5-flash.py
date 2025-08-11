def solve():
    """Index: 5624.
    Returns: the amount Jerry still has to pay.
    """
    # L1
    paid_two_months_ago = 12 # paid $12
    paid_more_last_month = 3 # paid $3 more
    paid_last_month = paid_two_months_ago + paid_more_last_month

    # L2
    total_paid_two_months = paid_two_months_ago + paid_last_month

    # L3
    total_debt = 50 # debt was $50 in all
    remaining_debt = total_debt - total_paid_two_months

    # FA
    answer = remaining_debt
    return answer