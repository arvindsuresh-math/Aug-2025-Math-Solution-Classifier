def solve():
    """Index: 519.
    Returns: the total amount Harrison spends on croissants in a year.
    """
    # L1
    regular_croissant_price = 3.50 # regular croissant on Saturdays for $3.50
    almond_croissant_price = 5.50 # almond croissant for $5.50 on Sundays
    weekly_pastry_total = regular_croissant_price + almond_croissant_price

    # L2
    weeks_per_year = 52 # one year, which is 52 weeks
    yearly_pastry_total = weeks_per_year * weekly_pastry_total

    # FA
    answer = yearly_pastry_total
    return answer