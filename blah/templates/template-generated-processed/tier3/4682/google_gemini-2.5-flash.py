def solve():
    """Index: 4682.
    Returns: the average star rating for Indigo Restaurant.
    """
    # L1
    num_five_star_reviews = 6 # six 5-star reviews
    five_star_value = 5 # 5-star reviews
    total_stars_five_star = num_five_star_reviews * five_star_value

    # L2
    num_four_star_reviews = 7 # seven 4-star reviews
    four_star_value = 4 # 4-star reviews
    total_stars_four_star = num_four_star_reviews * four_star_value

    # L3
    num_three_star_reviews = 4 # four 3-star reviews
    three_star_value = 3 # 3-star reviews
    total_stars_three_star = num_three_star_reviews * three_star_value

    # L4
    num_two_star_reviews = 1 # one 2-star review
    two_star_value = 2 # 2-star review
    total_stars_two_star = num_two_star_reviews * two_star_value

    # L5
    total_stars_received = total_stars_five_star + total_stars_four_star + total_stars_three_star + total_stars_two_star

    # L6
    total_reviews = 18 # 18 online customer reviews
    average_rating = total_stars_received / total_reviews

    # FA
    answer = average_rating
    return answer