def solve():
    """Index: 3006.
    Returns: the number of flavors Gretchen still needs to try.
    """
    # L1
    total_flavors = 100 # 100 different flavors
    two_years_ago_fraction_decimal = 0.25 # 1/4 of the flavors
    flavors_two_years_ago = total_flavors * two_years_ago_fraction_decimal

    # L2
    double_factor = 2 # double that amount
    flavors_last_year = flavors_two_years_ago * double_factor

    # L3
    total_flavors_tried_so_far = flavors_two_years_ago + flavors_last_year

    # L4
    flavors_to_try_this_year = total_flavors - total_flavors_tried_so_far

    # FA
    answer = flavors_to_try_this_year
    return answer