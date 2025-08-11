def solve():
    """Index: 6176.
    Returns: the total number of girls signed up to compete.
    """
    # L1
    total_kids_signed_up = 34 # 34 kids signed up
    girls_more_than_boys = 22 # 22 more girls than boys
    remaining_for_equal_split = total_kids_signed_up - girls_more_than_boys

    # L2
    divisor_for_equal_split = 2 # / 2
    boys_and_base_girls = remaining_for_equal_split / divisor_for_equal_split

    # L3
    total_girls = boys_and_base_girls + girls_more_than_boys

    # FA
    answer = total_girls
    return answer