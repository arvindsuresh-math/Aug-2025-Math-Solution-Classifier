def solve():
    """Index: 1845.
    Returns: the amount of money Julia is short to buy 4 of each type of CD.
    """
    # L1
    price_rock = 5 # rock and roll CDs are $5 each
    qty_each = 4 # buy 4 of each
    total_rock = price_rock * qty_each

    # L2
    price_pop = 10 # pop CDs are $10 each
    total_pop = price_pop * qty_each

    # L3
    price_dance = 3 # dance CDs are $3 each
    total_dance = price_dance * qty_each

    # L4
    price_country = 7 # country CDs are $7 each
    total_country = price_country * qty_each

    # L5
    total_needed = total_rock + total_pop + total_dance + total_country

    # L6
    julia_has = 75 # she only has 75 dollars
    money_short = total_needed - julia_has

    # FA
    answer = money_short
    return answer