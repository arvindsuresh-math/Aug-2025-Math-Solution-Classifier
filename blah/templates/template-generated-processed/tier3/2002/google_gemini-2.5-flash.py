def solve():
    """Index: 2002.
    Returns: the combined total number of circles and squares on Pete's flag.
    """
    # L1
    stars_on_us_flag = 50 # The United States flag has 50 stars
    half_stars = stars_on_us_flag / 2

    # L2
    less_than_half_stars = 3 # 3 less than half the number of stars
    num_circles = half_stars - less_than_half_stars

    # L3
    stripes_on_us_flag = 13 # 13 stripes
    twice_stripes = stripes_on_us_flag * 2

    # L4
    more_than_twice_stripes = 6 # six more than twice the number of stripes
    num_squares = twice_stripes + more_than_twice_stripes

    # L5
    total_circles_and_squares = num_circles + num_squares

    # FA
    answer = total_circles_and_squares
    return answer