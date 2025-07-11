def solve():
    """Index: 1793.
    Returns: the amount of money Dawn makes per hour.
    """
    # L1
    hours_per_painting = 2 # It takes Dawn 2 hours to paint 1 watercolor painting
    num_paintings = 12 # commissioned to paint a series of 12 paintings
    total_hours = hours_per_painting * num_paintings

    # L2
    total_earnings = 3600 # Dawn will earn $3,600.00 for these 12 paintings
    money_per_hour = total_earnings / total_hours

    # FA
    answer = money_per_hour
    return answer