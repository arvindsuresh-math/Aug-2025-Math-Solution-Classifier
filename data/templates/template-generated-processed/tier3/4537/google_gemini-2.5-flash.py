def solve():
    """Index: 4537.
    Returns: the amount of money Miranda saved per month.
    """
    # L1
    total_paid = 260 # paid $260 in total
    sister_contribution = 50 # gave her $50
    total_saved = total_paid - sister_contribution

    # L2
    months_saved = 3 # saved money for 3 months
    saved_per_month = total_saved / months_saved

    # FA
    answer = saved_per_month
    return answer