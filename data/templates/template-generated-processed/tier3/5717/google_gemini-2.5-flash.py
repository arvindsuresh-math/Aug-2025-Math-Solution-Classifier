def solve():
    """Index: 5717.
    Returns: the total number of cookies collected.
    """
    # L1
    abigail_boxes = 2 # Abigail collected 2 boxes
    cookies_per_box = 48 # each box contains 48 cookies
    abigail_cookies = abigail_boxes * cookies_per_box

    # L2
    quarter_denominator = 4 # 3 quarters of a box
    cookies_per_quarter_box = cookies_per_box / quarter_denominator

    # L3
    grayson_quarter_numerator = 3 # 3 quarters of a box
    grayson_cookies = cookies_per_quarter_box * grayson_quarter_numerator

    # L4
    olivia_boxes = 3 # Olivia collected 3 boxes
    olivia_cookies = cookies_per_box * olivia_boxes

    # L5
    total_cookies = abigail_cookies + grayson_cookies + olivia_cookies

    # FA
    answer = total_cookies
    return answer