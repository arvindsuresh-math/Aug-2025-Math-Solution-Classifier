def solve():
    """Index: 5555.
    Returns: the total number of stars Tilly counts.
    """
    # L1
    stars_east = 120 # 120 stars to the east
    multiplier_west = 6 # six times that number to the west
    stars_west = stars_east * multiplier_west

    # L2
    total_stars = stars_west + stars_east

    # FA
    answer = total_stars
    return answer