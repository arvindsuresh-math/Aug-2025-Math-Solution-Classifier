def solve():
    """Index: 3811.
    Returns: the total money Carmen made from selling cookies.
    """
    # L1
    samoas_boxes = 3 # three boxes of samoas
    samoas_price_per_box = 4 # $4 each
    green_house_earnings = samoas_boxes * samoas_price_per_box

    # L2
    thin_mints_boxes = 2 # two boxes of thin mints
    thin_mints_price_per_box = 3.50 # $3.50 each
    thin_mints_earnings = thin_mints_boxes * thin_mints_price_per_box

    # L3
    fudge_delights_price = 5 # one box of fudge delights for $5
    yellow_house_earnings = thin_mints_earnings + fudge_delights_price

    # L4
    sugar_cookies_boxes = 9 # nine boxes of sugar cookies
    sugar_cookies_price_per_box = 2 # $2 each
    brown_house_earnings = sugar_cookies_boxes * sugar_cookies_price_per_box

    # L5
    total_earnings = green_house_earnings + yellow_house_earnings + brown_house_earnings

    # FA
    answer = total_earnings
    return answer