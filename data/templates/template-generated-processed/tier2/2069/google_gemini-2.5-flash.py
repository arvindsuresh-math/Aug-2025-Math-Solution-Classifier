def solve():
    """Index: 2069.
    Returns: the number of shoes Page has now.
    """
    # L1
    initial_shoes = 80 # 80 pairs in her closet
    donation_percent_text = 30 # donate 30% of her collection
    donation_percent_decimal = 0.30 # .30*80
    percent_factor = 0.01 # WK
    donated_shoes = donation_percent_text * percent_factor * initial_shoes

    # L2
    shoes_after_donation = initial_shoes - donated_shoes

    # L3
    bought_shoes = 6 # buys 6 more pairs
    final_shoes = shoes_after_donation + bought_shoes

    # FA
    answer = final_shoes
    return answer