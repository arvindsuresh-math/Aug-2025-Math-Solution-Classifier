def solve():
    """Index: 6825.
    Returns: the total number of chocolate bars and soda cans Kayla bought.
    """
    # L1
    theresa_chocolate_bars = 12 # Theresa bought 12 chocolate bars
    twice_factor = 2 # twice the number of chocolate bars
    kayla_chocolate_bars = theresa_chocolate_bars / twice_factor

    # L2
    theresa_soda_cans = 18 # and 18 soda cans
    kayla_soda_cans = theresa_soda_cans / twice_factor

    # L3
    total_kayla_items = kayla_chocolate_bars + kayla_soda_cans

    # FA
    answer = total_kayla_items
    return answer