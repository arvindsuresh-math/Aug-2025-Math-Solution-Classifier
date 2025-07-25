from fractions import Fraction

def solve():
    """Index: 7076.
    Returns: the difference in money spent on cookies versus Oreos.
    """
    # L1
    oreo_ratio_part = 4 # ratio 4:9
    cookie_ratio_part = 9 # ratio 4:9
    total_ratio_parts = oreo_ratio_part + cookie_ratio_part

    # L2
    total_items = 65 # total number of items in the box is 65
    oreo_fraction = Fraction(oreo_ratio_part, total_ratio_parts)
    num_oreos = oreo_fraction * total_items

    # L3
    cost_per_oreo = 2 # each Oreo at $2
    total_cost_oreos = cost_per_oreo * num_oreos

    # L4
    num_cookies = total_items - num_oreos

    # L5
    cost_per_cookie = 3 # each cookie at $3
    total_cost_cookies = num_cookies * cost_per_cookie

    # L6
    difference_in_cost = total_cost_cookies - total_cost_oreos

    # FA
    answer = difference_in_cost
    return answer