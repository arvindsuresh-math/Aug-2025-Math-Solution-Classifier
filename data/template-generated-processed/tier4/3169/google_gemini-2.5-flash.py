def solve():
    """Index: 3169.
    Returns: the total amount John pays per year for grass cutting.
    """
    # L1
    max_height = 4 # When it gets to 4 inches
    cut_height = 2 # cuts it back down to 2 inches
    growth_before_cut = max_height - cut_height

    # L2
    growth_per_month = 0.5 # It grows .5 inches per month
    cut_frequency_months = growth_before_cut / growth_per_month

    # L3
    months_per_year = 12 # WK
    cuts_per_year = months_per_year / cut_frequency_months

    # L4
    cost_per_cut = 100 # It cost $100 to get his grass cut
    total_annual_cost = cost_per_cut * cuts_per_year

    # FA
    answer = total_annual_cost
    return answer