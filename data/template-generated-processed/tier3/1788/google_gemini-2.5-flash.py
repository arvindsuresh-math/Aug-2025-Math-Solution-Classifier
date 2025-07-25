def solve():
    """Index: 1788.
    Returns: the number of lychees remaining.
    """
    # L1
    total_lychees = 500 # harvested 500 lychees
    sold_fraction_numerator = 1 # half of them
    sold_fraction_denominator = 2 # half of them
    lychees_sold_at_market = (sold_fraction_numerator / sold_fraction_denominator) * total_lychees

    # L2
    remaining_lychees_after_market = total_lychees - lychees_sold_at_market

    # L3
    eaten_fraction_numerator = 3 # ate 3/5 of them
    eaten_fraction_denominator = 5 # ate 3/5 of them
    lychees_eaten_at_home = (eaten_fraction_numerator / eaten_fraction_denominator) * remaining_lychees_after_market

    # L4
    final_remaining_lychees = remaining_lychees_after_market - lychees_eaten_at_home

    # FA
    answer = final_remaining_lychees
    return answer