def solve():
    """Index: 214.
    Returns: the number of months ago they celebrated their 2nd anniversary.
    """
    # L1
    future_anniversary_years = 4 # 4th anniversary
    months_per_year = 12 # WK
    months_at_future_anniversary = future_anniversary_years * months_per_year

    # L2
    months_until_future_anniversary = 6 # In 6 months
    current_months_together = months_at_future_anniversary - months_until_future_anniversary

    # L3
    past_anniversary_years = 2 # 2nd anniversary
    months_at_past_anniversary = past_anniversary_years * months_per_year

    # L4
    months_difference = current_months_together - months_at_past_anniversary

    # FA
    answer = months_difference
    return answer