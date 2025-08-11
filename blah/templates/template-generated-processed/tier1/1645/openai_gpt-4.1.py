def solve():
    """Index: 1645.
    Returns: the amount of change Raine gets back from a $100 bill after her purchase.
    """
    # L1
    num_bracelets = 3 # three bracelets
    price_bracelet = 15 # bracelets at $15 each
    bracelets_total = num_bracelets * price_bracelet

    # L2
    num_necklaces = 2 # two gold heart necklaces
    price_necklace = 10 # gold heart necklace at $10
    necklaces_total = num_necklaces * price_necklace

    # L3
    price_mug = 20 # personalized coffee mug at $20
    mugs_total = price_mug # one coffee mug
    total_amount = bracelets_total + necklaces_total + mugs_total

    # L4
    bill_given = 100 # one hundred dollar bill
    change = bill_given - total_amount

    # FA
    answer = change
    return answer