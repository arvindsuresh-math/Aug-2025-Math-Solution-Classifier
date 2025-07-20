def solve():
    """Index: 7015.
    Returns: the number of posters Cassidy has now.
    """
    # L2
    posters_added_summer = 6 # six more posters
    posters_two_years_ago = 14 # had 14 posters
    double_factor = 2 # double the size
    posters_after_summer = double_factor * posters_two_years_ago

    # L3
    current_posters = posters_after_summer - posters_added_summer

    # FA
    answer = current_posters
    return answer