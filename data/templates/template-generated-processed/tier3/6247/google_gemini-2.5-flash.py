def solve():
    """Index: 6247.
    Returns: the total number of cookies that can fit in the box.
    """
    # L1
    ounces_per_pound = 16 # WK
    cookie_weight_ounces = 2 # each cookie weighs 2 ounces
    cookies_per_pound = ounces_per_pound / cookie_weight_ounces

    # L2
    box_capacity_pounds = 40 # His box can only hold 40 pounds of cookies
    total_cookies = box_capacity_pounds * cookies_per_pound

    # FA
    answer = total_cookies
    return answer