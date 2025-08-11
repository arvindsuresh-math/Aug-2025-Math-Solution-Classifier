def solve():
    """Index: 3859.
    Returns: the total potential revenue lost by the shop over 6 years.
    """
    # L1
    loss_per_day_val = 5 # 5 thousand dollars
    num_closed_days = 3 # closed for 3 days
    thousand = 1000 # WK
    total_loss_per_holiday = loss_per_day_val * num_closed_days * thousand

    # L2
    num_years = 6 # 6 years of activity
    total_revenue_lost = total_loss_per_holiday * num_years

    # FA
    answer = total_revenue_lost
    return answer