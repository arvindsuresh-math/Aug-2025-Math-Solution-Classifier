def solve():
    """Index: 467.
    Returns: the total number of miles Hadley walked in his boots.
    """
    # L1
    to_grocery = 2 # walked 2 miles to the grocery store
    two = 2 # WK
    one = 1 # WK
    to_pet = two - one

    # L2
    four = 4 # WK
    to_home = four - one

    # L3
    total_miles = to_grocery + to_pet + to_home

    # FA
    answer = total_miles
    return answer