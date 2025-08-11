def solve():
    """Index: 519.
    Returns: the total amount spent on croissants in a year.
    """
    # L1
    plain_croissant_cost = 3.50 # $3.50
    almond_croissant_cost = 5.50 # $5.50
    weekend_pastry_cost = plain_croissant_cost + almond_croissant_cost

    # L2
    weeks_in_year = 52 # 52 weeks
    total_annual_cost = weeks_in_year * weekend_pastry_cost

    # FA
    answer = total_annual_cost
    return answer