def solve():
    """Index: 2934.
    Returns: the number of screws in each pile.
    """
    # L1
    original_screws = 8 # Mary only has 8 screws on hand
    multiplier = 2 # needs to buy 2 times more
    total_screws = original_screws + (original_screws * multiplier)

    # L2
    num_sections = 4 # split the screws into four sections
    screws_per_pile = total_screws / num_sections

    # FA
    answer = screws_per_pile
    return answer